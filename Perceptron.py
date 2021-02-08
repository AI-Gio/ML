class Perceptron:
    inputs = None
    output = None

    def __init__(self, ID, weights, bias):
        """
        Initializes perceptron with needed attributes
        :param ID: Name of perceptron
        :param weights: list of weights (inputwise) (order of the elements should correspond with the order of inputs)
        :param bias: integer that stands for the bias
        """
        self.ID = ID
        self.weights = weights
        self.bias = bias

    def calc_output(self, inputs):
        """
        Calculates the output of the perceptron using the input values and corresponding weights and the bias
        to compare with the threshold
        :return: Boolean value
        """
        if len(inputs) != len(self.weights):
            raise ValueError("The amount of inputs and the amount of weights do not correspond")
        else:
            # multiplies input values with corresponding weights
            paths = [a * b for a, b in zip(inputs, self.weights)]
            # output gets a bitwise value by converting a boolean expression into an integer
            self.output = int((self.bias + sum(paths)) >= 0)
            self.inputs = inputs
            return self.output

    def __str__(self):
        return f"""id: {self.ID}, inputs: {self.inputs}, weights: {self.weights}, bias: {self.bias}, output: {self.output}
        """

    "__**== Getters and Setters ==**__"
    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID


    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights


    def get_bias(self):
        return self.bias

    def set_bias(self, bias):
        self.bias = bias


    def get_output(self):
        return self.output

    def set_output(self, output):
        self.output = output

# INVERT gate
P1 = Perceptron(ID=1, weights=[-1], bias=0)
print(P1.calc_output([1]))
print(P1)

# AND gate
P2 = Perceptron(ID=2, weights=[0.5, 0.5], bias=-1)
print(P2.calc_output([1,1]))
print(P2)

# OR gate
P3 = Perceptron(ID=3, weights=[1,1], bias=-1)
P3.calc_output([0,1])
print(P3)

# NOR gate
P4 = Perceptron(ID=4, weights=[-1, -1], bias=1)
P4.calc_output([1,0])
print(P4)
