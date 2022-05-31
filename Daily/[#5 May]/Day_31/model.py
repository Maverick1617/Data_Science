import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

device = "cuda:0" if torch.cuda.is_available() else "cpu"
learning_rate = 0.00001
momentum_val = 0.9


def create_model():

    class Model(nn.Module):

        def __init__(self):
            super(Model, self).__init__()
            # input layers
            self.input_layer = nn.Linear(3, 16)
            # Hidden layers
            self.fc1 = nn.Linear(16, 32)
            self.fc2 = nn.Linear(32, 16)
            # output layer
            self.output_layer = nn.Linear(16, 1)

        # forward pass
        def forward(self, x):
            x = F.relu(self.input_layer(x))
            x = F.relu(self.fc1(x))
            x = F.relu(F.dropout(self.fc2(x)))
            return self.output_layer(x)

    net = Model()
    optimizer = torch.optim.SGD(net.parameters(),
                                lr=learning_rate,
                                momentum=momentum_val)
    loss = nn.BCEWithLogitsLoss()
    return net, optimizer, loss


def train_model(train_loader, test_loader, epochs=5):
    print("Training on", device)
    model, optimizer, Loss = create_model()
    model = model.to(device)
    train_acc = []
    test_acc = []
    train_loss = []
    test_loss = []
    for epoch in range(epochs):
        batch_acc = []
        batch_loss = []
        for x, y in train_loader:
            # Forward pass
            x = x.to(device)
            y = y.to(device)
            yh = model(x)
            loss = Loss(yh, y)
            # Backward propagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # Calculating Batch performance
            corrects = ((yh >= 0.5) == y).float()
            batch_acc.append(100 * torch.mean(corrects).item())
            batch_loss.append(loss.item())

        # Calculating total batch performance
        train_acc.append(np.mean(batch_acc))
        train_loss.append(np.mean(batch_loss))
        # Evaluating on test loader
        x, y = next(iter(test_loader))
        x = x.to(device)
        y = y.to(device)
        with torch.no_grad():
            yh = model(x)
            loss = Loss(yh, y)
        corrects = ((yh >= 0.5) == y).float()
        test_acc.append(100 * torch.mean(corrects).item())
        test_loss.append(loss.item())
        print(f"Epoch: {epoch + 1}, Train Acc: {train_acc[-1]}, Test Acc: {test_acc[-1]}")
    return model, train_acc, test_acc, train_loss, test_loss


if __name__ == "__main__":
    print("Simple Test")
    data = torch.tensor([[1, 2, 2],
                         [1, 4, 2]]).float()
    model = create_model()[0]
    model = model.to(device)
    data = data.to(device)
    yh = model(data)
    print(yh)
