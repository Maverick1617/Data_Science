# Neural Network

```python
from dense import Dense
from activation import Tanh
from loss import mse, mse_prime
import numpy as np
from network import train

"""
    XOR example
"""

X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))

model = [
    Dense(2, 3),
    Tanh(),
    Dense(3, 1),
    Tanh()
]
epochs = 10000
train(model, mse, mse_prime, X, Y, epochs)

```
