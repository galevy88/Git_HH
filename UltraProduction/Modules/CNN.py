from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from torch import nn, optim
import torch


import torch
from torch import nn


import numpy as np

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.conv1 = nn.Conv1d(1, 64, kernel_size=5, stride=1, padding=2)
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool1d(kernel_size=2)
        
        self.conv2 = nn.Conv1d(64, 128, kernel_size=5, stride=1, padding=2)
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool1d(kernel_size=2)

        # Fully connected layer
        self.fc1 = nn.Linear(128 * 300, 512)  # This should be 128 * (input_size/4)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(512, 2)  # two output classes: 0 and 1
        
    def forward(self, x):
        x = x.unsqueeze(1)  # add a dimension for the number of channels
        out = self.conv1(x)
        out = self.relu1(out)
        out = self.maxpool1(out)
        out = self.conv2(out)
        out = self.relu2(out)
        out = self.maxpool2(out)

        # Flatten the tensor output by the convolutional layers
        out = out.view(out.size(0), -1)

        # Fully connected layers
        out = self.fc1(out)
        out = self.relu3(out)
        out = self.fc2(out)
        
        return out


# Define a Dataset
class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return torch.tensor(self.data[idx][1]), self.data[idx][2]  # Return the numpy array and the label

def prepare_data(samples):
    samples_train, samples_test = train_test_split(samples, test_size=0.1, random_state=42)
    train_dataset = MyDataset(samples_train)
    test_dataset = MyDataset(samples_test)
    return train_dataset, test_dataset


def define_model_and_optimizer():
    model = CNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    return model, criterion, optimizer


def train_model(model, criterion, optimizer, train_loader, epochs):
    for epoch in range(epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs.float())
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Loss after epoch {epoch}: {loss.item()}")
    return model


def evaluate_model(model, test_loader):
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for inputs, labels in test_loader:
            outputs = model(inputs.float())
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        print(f"Accuracy of the model on test data: {100 * correct / total}%")




def CNN_train(samples):
    train_dataset, test_dataset = prepare_data(samples)
    model, criterion, optimizer = define_model_and_optimizer()
    train_loader = DataLoader(train_dataset, batch_size=len(train_dataset), shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=len(test_dataset), shuffle=True)
    model = train_model(model, criterion, optimizer, train_loader, epochs=100)
    evaluate_model(model, test_loader)
    return model

def CNN_predict(model, cell, path):
    # convert numpy array to PyTorch tensor and add batch dimension
    cell_tensor = torch.tensor(cell[1]).unsqueeze(0).float()

    outputs = model(cell_tensor)

    predicted_class_index = torch.argmax(outputs[0]).item()

    class_labels = {0: "N", 1: "MH"}

    MP_path = path + f"/{cell[0]}/{cell[0]}_sample.csv"

    return class_labels[predicted_class_index], MP_path


