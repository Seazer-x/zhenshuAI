import os
import cv2
import numpy as np

from torch.utils.data.dataset import Dataset


# 定义手写数字数据集类
class MnistDataset(Dataset):
    def __init__(self, root, train: bool = True):
        # 初始化基类
        super(MnistDataset, self).__init__()
        # 初始化数据集
        self.dataset = []
        # 判定要创建的数据集类型
        folder = "TRAIN" if train else "TEST"
        # 获取数据文件夹
        classes = os.path.join(root, folder)
        # tag:类别
        for tag in os.listdir(classes):
            # 获取图片文件夹路径
            image_folder = os.path.join(root, folder, tag)
            for item in os.listdir(image_folder):
                # 获取图片绝对路径
                abs_path = os.path.join(image_folder, item)
                # print(abs_path)
                # 将图片和tag添加到数据集中
                self.dataset.append((abs_path, tag))

    def __len__(self):
        # 获取dataset大小
        return len(self.dataset)

    def __getitem__(self, index):
        data = self.dataset[index]
        # 获取图片路径
        img_path = data[0]
        img = cv2.imread(img_path, 0)
        # reshape图片为一维
        img = img.reshape(-1)
        # 归一化
        img = img // 255
        one_hot = np.zeros(10)
        tag = data[1]
        # 创建one_hot编码
        one_hot[int(tag)] = 1.0
        return np.float32(img), np.float32(one_hot)


if __name__ == '__main__':
    dataset = MnistDataset("MNIST_IMG", train=False)
    print(len(dataset))
    print(dataset[1])
