"""
For documentation of different layers, please refer to torch.nn
https://pytorch.org/docs/stable/nn.html
"""

import torch
from torch import nn


class OneLayerNN(nn.Module):

    def __init__(self, input_features=11):
        """
        Initializes a liner layer.
        :param input_features: The number of features of each sample.
        """
        super().__init__()

        # TODO: Initialize a linear layer. HINT: torch.nn.Linear
        self.linear = nn.Linear(input_features, 1)


    def forward(self, X):
        """
        Applies the linear layer defined in __init__() to input features X.
        :param X: 2D torch tensor of shape [n, 11], where n is batch size.
            Represents features of a batch of data.
        :return: 2D torch tensor of shape [n, 1], where n is batch size.
            Represents prediction of wine quality.
        """

        # TODO: Apply the linear layer defined in __init__() to input features X

        return self.linear(X)

class TwoLayerNN(nn.Module):

    def __init__(self, input_features=11, hidden_size=32):
        """
        Initializes model layers.
        :param input_features: The number of features of each sample.
        :param hidden_size: The number of units in the hidden layer.
        """
        super().__init__()

        # hidden, linear 
        self.hidden_size = hidden_size
        self.fc1 = nn.Linear(input_features, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 1)

        self.sigmoid = nn.Sigmoid()

    def forward(self, X):
        """
        Applies the layers defined in __init__() to input features X.
        :param X: 2D torch tensor of shape [n, 11], where n is batch size.
            Represents features of a batch of data.
        :return: 2D torch tensor of shape [n, 1], where n is batch size.
            Represents prediction of wine quality.
        """

        # Apply first linear layer and activation function
        hidden = self.sigmoid(self.fc1(X))

        # Apply second linear layer
        output = self.fc2(hidden)

        return output



class CNN(nn.Module):

    def __init__(self, input_channels=1, class_num=10):
        """
        Initializes model layers.
        :param input_channels: The number of channels of each input image (e.g., 1 for grayscale, 3 for RGB).
        :param class_num: The number of categories.
        """
        super().__init__()

        # Initialize convolutional layers
        self.conv_lay_1 = nn.Conv2d(input_channels, 16, kernel_size=3, padding=1)
        self.conv_lay_2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)

        # activation functions 
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

        # flatten 
        self.flatten = nn.Flatten()

        # these are the linear layers 
        self.lin_1 = nn.Linear(2048, 128)
        self.lin_2 = nn.Linear(128, class_num)

    def forward(self, X):
        """
        Applies the layers defined in __init__() to input features X.
        :param X: 4D torch tensor of shape [n, 1, 8, 8], where n is batch size.
            Represents a batch of 8 * 8 gray scale images.
        :return: 2D torch tensor of shape [n, 10], where n is batch size.
            Represents logits of different categories.
        """

        # Apply the layers defined in __init__() to input features X
        X = self.relu(self.conv_lay_1(X))
        X = self.relu(self.conv_lay_2(X))
        X = self.flatten(X)
        X = self.sigmoid(self.lin_1(X))
        X = self.lin_2(X)

        return X



def train(model, dataloader, loss_func, optimizer, num_epoch, correct_num_func=None, print_info=True):
    """
    Trains the model for `num_epoch` epochs.
    :param model: A deep model.
    :param dataloader: Dataloader of the training set. Contains the training data equivalent to ((Xi, Yi)),
        where (Xi, Yi) is a batch of data.
        X: 2D torch tensor for UCI wine and 4D torch tensor for MNIST.
        X: 2D torch tensor for UCI wine and 1D torch tensor for MNIST, containing the corresponding labels
            for each example.
        Refer to the Data Format section in the handout for more information.
    :param loss_func: An MSE loss function for UCI wine and a cross entropy loss for MNIST.
    :param optimizer: An optimizer instance from torch.optim.
    :param num_epoch: The number of epochs we train our network.
    :param correct_num_func: A function to calculate how many samples are correctly classified.
        You need to implement correct_predict_num() below.
        To train the CNN model, we also want to calculate the classification accuracy in addition to loss.
    :param print_info: If True, print the average loss (and accuracy, if applicable) after each epoch.
    :return:
        epoch_average_losses: A list of average loss after each epoch.
            Note: different from HW10, we will return average losses instead of total losses.
        epoch_accuracies: A list of accuracy values after each epoch. This is applicable when training on MNIST.
    """

    # Initializing variables
    epoch_average_losses = [] 
    epoch_accuracy_values = []  

    # Tell the model we are in the training phase.
    model.train()

    # train network for num_epochs
    for epoch in range(num_epoch):

        epoch_loss_sum = 0  
        epoch_correct_num = 0  

        # iteration through the batches 
        for X, Y in dataloader: 

            # Run a forward pass and get model output
            mod_out = model(X) 

            # Set all gradients to zero
            optimizer.zero_grad()  

            # Calculate loss of this batch
            batch_loss = loss_func(mod_out, Y)  

            # Run a backward pass
            batch_loss.backward()  

            optimizer.step()  

            num_samples = X.shape[0];
            epoch_loss_sum += batch_loss.item() * num_samples  # Increase epoch_loss_sum.


            # Calculate the number of correct predictions for CNN on MNIST
            if correct_num_func:  
                epoch_correct_num += correct_num_func(mod_out, Y)

        # Append the average loss of the current epoch
        epoch_average_losses.append(epoch_loss_sum / len(dataloader.dataset)) 


        # Calculate average accuracy for CNN on MNIST if correct_num_func is not None
        if correct_num_func:  
            epoch_accuracy_values.append(epoch_correct_num / len(dataloader.dataset))


        # Print the loss after every epoch. Print accuracies if specified
        if print_info:  
            print('Epoch: {} | Loss: {:.4f} '.format(epoch, epoch_loss_sum / len(dataloader.dataset)), end="")
            if correct_num_func:
                print('Accuracy: {:.4f}%'.format(epoch_correct_num / len(dataloader.dataset) * 100)),


    # TODO: When correct_num_func is None, only return a list of average losses.
    #  When correct_num_func is not None, return a list of average losses and a list of accuracies.
    if correct_num_func is None:
        return epoch_average_losses
    else:
        return epoch_average_losses, epoch_accuracy_values


def test(model, dataloader, loss_func, correct_num_func=None):
    """
    Tests the model.
    :param model: A deep model.
    :param dataloader: Dataloader of the testing set. Contains the testing data equivalent to ((Xi, Yi)),
        where (Xi, Yi) is a batch of data.
        X: 2D torch tensor for UCI wine and 4D torch tensor for MNIST.
        X: 2D torch tensor for UCI wine and 1D torch tensor for MNIST, containing the corresponding labels
            for each example.
        Refer to the Data Format section in the handout for more information.
    :param loss_func: An MSE loss function for UCI wine and a cross entropy loss for MNIST.
    :param correct_num_func: A function to calculate how many samples are correctly classified.
        You need to implement correct_predict_num() below.
        To test the CNN model, we also want to calculate the classification accuracy in addition to loss.
    :return:
        Average loss.
        Average accuracy. This is applicable when testing on MNIST.
    """

    # Initializing variables
    sum_of_losses_epoch = 0
    num_correct_pred = 0

    # Tell the model we are in the testing phase
    model.eval()

    # During testing, we don't need to calculate gradients
    with torch.no_grad():
        for X, Y in dataloader:

            # Run a forward pass and get model output
            mod_out = model(X)

            # Calculate loss of this batch
            batch_loss = loss_func(mod_out, Y)

            # Increase loss sum by (loss * #samples in the current batch)
            num_samples = X.shape[0]
            sum_of_losses_epoch += batch_loss.item() * num_samples

            # When correct_num_func is not None, calculate the number of correct predictions for CNN on MNIST
            if correct_num_func is not None:
                num_correct_pred += correct_num_func(mod_out, Y)

    # When correct_num_func is None, return average loss
    if correct_num_func is None:
        return sum_of_losses_epoch / len(dataloader.dataset)
    else:
        # When correct_num_func is not None, return average loss and accuracy
        accuracy = num_correct_pred / len(dataloader.dataset)
        return sum_of_losses_epoch / len(dataloader.dataset), accuracy



def correct_predict_num(logit, target):
    """
    Returns the number of correct predictions.
    :param logit: 2D torch tensor of shape [n, class_num], where
        n is the number of samples, and class_num is the number of classes (10 for MNIST).
        Represents the output of CNN model.
    :param target: 1D torch tensor of shape [n],  where n is the number of samples.
        Represents the ground truth categories of images.
    :return: A python scalar. The number of correct predictions.
    """

    # Get the predicted category index
    predicted_index = torch.argmax(logit, dim=1).long()  
    # Count the number of correct predictions
    return torch.sum(predicted_index == target.long()).item()

