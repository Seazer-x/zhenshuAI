import torch
from rich.progress import *
from torch import nn, optim
from torch.nn.functional import one_hot
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import *

from All_connaction import Net_V1

train_data = MNIST(download=True, root="./dataset", train=True, transform=ToTensor())
test_data = MNIST(download=True, root="./dataset", train=False, transform=ToTensor())
# print("训练集data的shape:", train_data.data.shape)
# print("测试集data的shape:", test_data.data.shape)
# print("训练集targets的shape:", train_data.targets.shape)
# print("测试集targets的shape:", test_data.targets.shape)
# print("训练集data的第一个数据:", train_data.data[0])
# print("训练集targets的第一个数据:", train_data.targets[0])
# ToPILImage()(train_data.data[0]).show()
train_loader = DataLoader(train_data, batch_size=512, shuffle=True)
test_loader = DataLoader(test_data, batch_size=512, shuffle=True)
loss_func = nn.MSELoss()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
progress = Progress()

if __name__ == '__main__':
    print(device)
    net = Net_V1(28, 28)
    net = net.to(device)
    opt = optim.Adam(net.parameters())
    with progress:
        epoch_prog = progress.add_task('[cyan]Epoch...', total=100)
        for epoch in range(100):
            # train_prog = progress.add_task('[red]Training...', total=117)
            progress.refresh()
            for i, (img, label) in enumerate(train_loader):
                img = img.reshape(-1, 28 * 28)
                label = one_hot(label, 10).float()
                img = img.to(device)
                label = label.to(device)
                net.train()
                out = net(img)
                opt.zero_grad()
                loss = loss_func(out, label)
                loss.backward()
                opt.step()
                # progress.update(train_prog, advance=1)
                if (i + 1) % (60000 // 512) == 0:
                    print("第", epoch + 1, "次训练loss: %.7f" % loss.item())
            progress.update(epoch_prog, advance=1)
            if (epoch + 1) % 10 == 0:
                torch.save(net.state_dict(), f"weights/{epoch+1}.pt")

            for i, (img, label) in enumerate(test_loader):
                img = img.reshape(-1, 28 * 28)
                label = one_hot(label, 10).float()
                img = img.to(device)
                label = label.to(device)
                net.train()
                out = net(img)
                loss = loss_func(out, label)
                if (i + 1) % (10000 // 512) == 0:
                    print("第", epoch + 1, "次测试loss: %.7f" % loss.item())
