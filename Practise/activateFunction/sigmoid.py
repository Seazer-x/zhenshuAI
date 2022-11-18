import torch

a = torch.tensor([0.433, 0.343, 0.56], dtype=torch.float)
b = torch.softmax(a, dim=0)
print(b)
print(torch.sum(b))
