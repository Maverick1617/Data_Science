from layer import Layer
import numpy as np


class Dense(Layer):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.weights = np.random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)

    def forward(self, input_data):
        self.input = input_data
        return np.dot(self.weights, self.input) + self.bias

    def backward(self, output_gradient, learning_rate):
        wg = np.dot(output_gradient, self.input.T)
        self.weights -= learning_rate * wg
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights.T, output_gradient)
