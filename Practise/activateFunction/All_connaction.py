import torch
from PIL import Image
from torch import nn


class Net_V1(nn.Module):
    def __init__(self, img_w, img_h):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(img_w * img_h, 512),
            nn.Linear(512, 256),
            nn.Linear(256, 128),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.Linear(32, 10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.layer(x)


if __name__ == '__main__':
    image_path = input("图片路径:") or "wallhaven-1p8lk9.jpg"
    image = Image.open(image_path)
    w, h = image.size
    image.thumbnail((w // 2, h // 2))
    w, h = image.size
    img_array = image.convert("RGB").getdata()
    image_tensor = torch.tensor(img_array, dtype=torch.float32).view(w * h * 3)
    net = Net_V1(w, h)
    output = net.forward(image_tensor)
    print("\n", output)

