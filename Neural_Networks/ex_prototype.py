# X (inputs) -> [weights] -> weighted sum -> sigmoid -> prediction

import numpy as np


X = np.array([0.5, 0.6, 0.7])
y = np.array([1])

weights = np.array([0.3, 0.2, 0.4])
bias = 0.0

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


# hyperparameters
epochs = 10
learning_rate = 0.1


for epoch in range(epochs):
    # forward pass
    weighted_sum = np.dot(X, weights)
    prediction = sigmoid(weighted_sum)

    #MSE
    loss = np.mean(np.square(prediction - y))

    # backpropagation
    d_loss_prediction = -2 * (y - prediction)
    d_prediction_d_weighted_sum = sigmoid_derivative(weighted_sum)
    d_weighted_sum_d_weights = X
    d_weighted_sum_d_bias = 1

    # gradients
    gradient = d_loss_prediction * d_prediction_d_weighted_sum * d_weighted_sum_d_weights
    gradient_bias = d_loss_prediction * d_prediction_d_weighted_sum * d_weighted_sum_d_bias

    weights -= learning_rate * gradient
    bias -= learning_rate * gradient_bias

    print(f'Epoch {epoch + 1} / {epochs}. Loss: {loss}')

print(f'Final weights: {weights}')
print(f'Final bias: {bias}')

