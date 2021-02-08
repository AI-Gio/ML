class Perceptron:

    def __init__(self, ID, t, inputs, weights, bias):
        """
        Initializes perceptron with needed attributes
        :param ID: Name of perceptron
        :param t: threshold
        :param inputs: list of inputs
        :param weights: list of weights (inputwise) (order of the elements should correspond with the order of inputs)
        :param bias: integer that stands for the bias
        """
        self.ID = ID
        self.t = t
        self.inputs = inputs
        self.weights = weights
        self.bias = bias

    def calc_output(self):
        """
        Calculates the output of the perceptron using the input values and corresponding weights and the bias
        to compare with the threshold
        :return: Boolean value
        """
        if len(self.inputs) != len(self.weights):
            raise ValueError("The amount of inputs and the amount of weights do not correspond")
        else:
            # multiplies input values with corresponding weights
            paths = [a * b for a, b in zip(self.inputs, self.weights)]
            output = (self.bias + sum(paths)) >= self.t
            return output

    def __str__(self):
        return f"""
        id: {self.ID}
        inputs: {self.inputs}
        weights: {self.weights}
        threshold: {self.t}
        output: {self.calc_output()}
        """

    "__**== Getters and Setters ==**__"
    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID


    def get_t(self):
        return self.t

    def set_t(self, t):
        self.t = t


    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights


    def get_bias(self):
        return self.bias

    def set_bias(self, bias):
        self.bias = bias


    def get_inputs(self):
        return self.inputs

    def set_inputs(self, inputs):
        self.inputs = inputs


    def get_output(self):
        return self.output

    def set_output(self, output):
        self.output = output

# INVERT gate
P1 = Perceptron(1, -0.5, [1], [-1], 0)
print(P1)

# AND gate
P2 = Perceptron(2, 1, [1,1], [0.5, 0.5], 0)
print(P2)

# OR gate
P3 = Perceptron(3, 0.5, [0, 0], [0.5, 0.5], 0)
print(P3)