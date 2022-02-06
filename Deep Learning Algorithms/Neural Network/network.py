def predict(network, x):
    op = x
    for l in network:
        op = l.forward(op)
    return op


def train(network, loss, loss_prime, x_train, y_train, epochs=5, lr=0.01, verbose=True):
    for e in range(epochs):
        error = 0
        for x, y in zip(x_train, y_train):
            op = predict(network, x)
            error += loss(y, op)
            grad = loss_prime(y, op)
            for l in reversed(network):
                grad = l.backward(grad, lr)
        error /= len(x_train)
        if verbose:
            print(f"{e + 1}/{epochs}, error: {error}")
