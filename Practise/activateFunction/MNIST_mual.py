from torch import nn, optim
from torch.nn.functional import one_hot
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor


class Net(nn.Module):
    def __init__(self, img_w, img_h):
        super(Net, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(img_w * img_h, 512),
            nn.Linear(512, 256),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.Linear(64, 32),
            nn.Linear(32, 10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.layer(x)


train_data = MNIST(root="./data", train=True, transform=ToTensor(), download=True)
test_data = MNIST(root="./data", train=False, transform=ToTensor(), download=True)

train_loader = DataLoader(train_data, batch_size=512, shuffle=True)
test_loader = DataLoader(test_data, batch_size=512, shuffle=True)

if __name__ == '__main__':
    net = Net(28, 28)
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    for epoch in range(1000):
        for i, (img, label) in enumerate(train_loader):
            img = img.reshape(-1, 28 * 28)
            label = one_hot(label, 10).float()
            net.train()
            out = net(img)
            loss = loss_func(out, label)
            opt.zero_grad()
            loss.backward()
            opt.step()
            if (i+1) % (60000 // 512) == 0:
                print("第", epoch + 1, "次训练loss", loss.item())

        for i, (img, label) in enumerate(test_loader):
            img = img.reshape(-1, 28 * 28)
            label = one_hot(label, 10).float()
            net.eval()
            out = net(img)
            loss = loss_func(out, label)
            if (i+1) % (10000 // 512) == 0:
                print("第", epoch + 1, "次测试loss", loss.item())
