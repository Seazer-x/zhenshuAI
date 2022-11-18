import os

from rich.progress import Progress

import torch.cuda
from torch import optim
from torch.utils.data import DataLoader

from MnistDataSet import MnistDataset
from Net import MnistNet


class Train:
    def __init__(self, root, img_size=(100, 100), load_weight=None):
        # 获取绝对路径
        root = os.path.abspath(root)
        # 创建训练集
        self.train_dataset = MnistDataset(root)
        # 创建训练数据加载器
        self.train_loader = DataLoader(self.train_dataset, batch_size=512, shuffle=True)
        # 创建测试集
        self.test_dataset = MnistDataset(root, train=False)
        # 创建测试数据加载器
        self.test_loader = DataLoader(self.train_dataset, batch_size=512, shuffle=True)

        # 初始化网络
        self.net = MnistNet(img_size[0], img_size[1])
        if load_weight is not None:
            weight_path = os.path.abspath("weights")
            weight = os.path.join(weight_path, str(load_weight * 10) + ".pt")
            self.net.load_state_dict(torch.load(weight))

        # 初始化device
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # 将网络模型转移到device
        self.net.to(self.device)

        # 初始化优化器
        self.opt = optim.Adam(self.net.parameters())

        # 如果weights文件夹不存在则创建
        weight_path = os.path.join(os.path.curdir, "weights")
        if not os.path.exists(weight_path):
            os.makedirs(weight_path)

        # 初始化progress
        self.progress = Progress()

    # 魔法函数
    def __call__(self, *args, **kwargs):
        # 获取参数的第一个作为训练次数
        epochs = args[0]
        print("开始训练...")
        with self.progress:
            train_progress = self.progress.add_task('[cyan]Training...', total=epochs)
            for epoch in range(epochs):
                # 初始化sum_loss
                sum_loss = 0
                for i, (img, tag) in enumerate(self.train_loader):
                    # 将训练数据转移到device
                    img, tag = img.to(self.device), tag.to(self.device)
                    # 开启训练模式，
                    self.net.train()
                    # 训练网络模型
                    out = self.net(img)
                    # 计算损失
                    loss = torch.mean((out - tag) ** 2)
                    # 每一轮的损失求和
                    sum_loss += loss.item()
                    # 清除梯度
                    self.opt.zero_grad()
                    # 反向求导，计算w，b
                    loss.backward()
                    self.opt.step()
                self.progress.update(train_progress, advance=1)
                avg_loss = sum_loss / len(self.train_loader)
                print(f"第{epoch + 1}次训练loss : {avg_loss}")
                if (epoch + 1) % 10 == 0:
                    torch.save(self.net.state_dict(), f"weights/{epoch + 1}.pt")

    def test(self, *args):
        # 获取参数的第一个作为测试次数
        epochs = args[0]
        # 获取参数的第二个作测试权重
        weight_path = "weights"
        weight_path = os.path.abspath(weight_path)
        file_list = os.listdir(weight_path)
        files_len = len(file_list)
        # 权重路径
        weight = os.path.join(weight_path, file_list[files_len - 1])
        self.net.load_state_dict(torch.load(weight))
        print("开始测试...")
        with self.progress:
            test_progress = self.progress.add_task('[cyan]Evaluating...', total=epochs)
            for epoch in range(epochs):
                sum_loss = 0
                for i, (img, tag) in enumerate(self.train_loader):
                    img, tag = img.to(self.device), tag.to(self.device)
                    # 开启测试模式
                    self.net.eval()
                    # 预测结果
                    out = self.net(img)
                    # 预测损失
                    loss = torch.mean((out - tag) ** 2)
                    sum_loss += loss.item()
                self.progress.update(test_progress, advance=1)
                # 每一轮测试损失
                avg_loss = sum_loss / len(self.train_loader)
                print(f"第{epoch + 1}次测试loss : {avg_loss}")


if __name__ == '__main__':
    train = Train("MNIST_IMG", (28, 28))
    epoch_num = input("请输入要训练的次数：(默认100次)") or 100
    weight_num = 0
    if len(os.listdir("weights")) != 0:
        flag = input("是否加载已训练的权重？：(默认不加载)1.是") or "2"
        if flag == "1":
            weight_num = input("选择第几十次的训练权重：(例如：输入1则加载10.pt)")
    train(int(epoch_num), int(weight_num) if weight_num != 0 else 0)
    # train.test(10)
