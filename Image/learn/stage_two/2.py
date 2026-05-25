import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# ===== 1. 加载数据 =====
# MNIST是6万张手写数字图片，28x28灰度图，0-9共10类
transform = transforms.Compose([
    transforms.ToTensor(),  # 把PIL图片转为PyTorch张量，值从0-255缩放到0-1
    transforms.Normalize((0.1307,), (0.3081,))  # 标准化，让数据均值为0方差为1
])

train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_data  = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader  = DataLoader(test_data, batch_size=64, shuffle=False)

print(f"训练集大小: {len(train_data)}，测试集大小: {len(test_data)}")

# ===== 2. 定义模型 =====
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 128)  # 输入784个像素，输出128个特征
        self.fc2 = nn.Linear(128, 64)     # 128 → 64
        self.fc3 = nn.Linear(64, 10)      # 64 → 10（对应0-9十个数字）
        self.relu = nn.ReLU()             # 激活函数，引入非线性

    def forward(self, x):
        x = x.view(-1, 28*28)  # 把28x28的图像展平成784维向量
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)  # 最后一层不用激活，CrossEntropyLoss会自动处理
        return x

model = SimpleNet()
print(f"模型参数量: {sum(p.numel() for p in model.parameters()):,}")

# ===== 3. 定义损失函数和优化器 =====
criterion = nn.CrossEntropyLoss()  # 分类问题最常用的损失函数
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam优化器

# ===== 4. 训练模型 =====
def train_one_epoch():
    model.train()
    total_loss = 0
    correct = 0
    for images, labels in train_loader:
        optimizer.zero_grad()        # 清零梯度
        outputs = model(images)      # 前向传播
        loss = criterion(outputs, labels)  # 计算损失
        loss.backward()              # 反向传播
        optimizer.step()             # 更新参数
        
        total_loss += loss.item()
        correct += (outputs.argmax(dim=1) == labels).sum().item()
    
    avg_loss = total_loss / len(train_loader)
    accuracy = 100 * correct / len(train_data)
    return avg_loss, accuracy

# ===== 5. 测试模型 =====
def test():
    model.eval()
    correct = 0
    with torch.no_grad():  # 测试时不需要计算梯度
        for images, labels in test_loader:
            outputs = model(images)
            correct += (outputs.argmax(dim=1) == labels).sum().item()
    return 100 * correct / len(test_data)

# ===== 6. 开始训练 =====
print("\n开始训练...")
for epoch in range(10):  # 训练5轮
    loss, train_acc = train_one_epoch()
    test_acc = test()
    print(f"Epoch {epoch+1}/5 | 训练损失: {loss:.4f} | 训练准确率: {train_acc:.2f}% | 测试准确率: {test_acc:.2f}%")

print("\n✅ 训练完成！一个简单的神经网络已经学会了识别手写数字。")

# ===== 7. 可视化预测结果 =====
model.eval()
images, labels = next(iter(test_loader))
with torch.no_grad():
    outputs = model(images[:8])
    preds = outputs.argmax(dim=1)

fig, axes = plt.subplots(2, 4, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(images[i].squeeze(), cmap='gray')
    ax.set_title(f"预测: {preds[i].item()} | 真实: {labels[i].item()}")
    ax.axis('off')
plt.tight_layout()
plt.show()