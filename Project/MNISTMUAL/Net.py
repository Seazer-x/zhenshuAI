from torch import nn


# 定义全连接网络
class MnistNet(nn.Module):
    def __init__(self, img_w, img_h):
        super(MnistNet, self).__init__()
        self.layer = nn.Sequential(
            # 全连接层
            nn.Linear(img_w * img_h, 512),
            #  ReLU激活函数
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 10),
            # 使用Softmax激活函数后输出
            nn.Softmax(dim=1)
        )

    # 定义前向传播
    def forward(self, x):
        return self.layer(x)
