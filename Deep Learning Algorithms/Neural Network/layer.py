class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward(self, input_data):
        pass

    def backward(self, output_gradient, learning_rate):
        pass
