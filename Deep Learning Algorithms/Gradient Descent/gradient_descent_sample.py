import numpy as np

# data points
X = [0.5, 2.5]
Y = [0.2, 0.9]


# sigmoid with parameters w, b
def sigmoid(w, b, x):
    return 1.0 / (1.0 + np.exp(-(w * x + b)))


def error(w, b):
    total_error = 0.0
    for x, y in zip(X, Y):
        fx = sigmoid(w, b, x)
        total_error += 0.5 * (fx - y) ** 2
    return total_error


def gradient_b(w, b, x, y):
    fx = sigmoid(w, b, x)
    return (fx - y) * fx * (1 - fx)


def gradient_w(w, b, x, y):
    fx = sigmoid(w, b, x)
    return (fx - y) * fx * (1 - fx) * x


def gradient_descent():
    w, b, eta, epochs = -2, -2, 1.0, 1000
    for i in range(epochs):
        dw, db = 0, 0
        for x, y in zip(X, Y):
            dw += gradient_w(w, b, x, y)
            db += gradient_b(w, b, x, y)
        w -= eta * dw
        b -= eta * db
        print("Epoch", i + 1, ",Error: ", error(w, b))
    return


gradient_descent()
