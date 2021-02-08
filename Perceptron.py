class Perceptron:
    inputs = None
    output = None

    def __init__(self, weights, bias):
        """
        Initializes perceptron with needed attributes
        :param weights: list of weights (inputwise) (order of the elements should correspond with the order of inputs)
        :param bias: integer that stands for the bias
        """
        self.weights = weights
        self.bias = bias

    def calc_output(self, inputs):
        """
        Calculates the output of the perceptron using the input values and corresponding weights and the bias
        to compare with the threshold
        :param inputs: a list with 0's and 1's
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

    def give_gate(self, gateName, n_inputs):
        """
        Takes the amount of inputs and specifies what preset node to take
        :param gateName: A list with string that contain gate names
        :return: a Perceptron with the correct weights and bias
        """
        gates = {
        "INVERT": Perceptron(weights=[-1], bias=0),
        "AND": Perceptron(weights=[0.5 for i in range(n_inputs)], bias=n_inputs * -0.5),
        "OR": Perceptron(weights=[0.5 for i in range(n_inputs)], bias=-0.5),
        "NOR": Perceptron(weights=[-1 for i in range(n_inputs)], bias=0),
        "NAND": Perceptron(weights=[-1 for i in range(n_inputs)], bias=n_inputs-1)
        }
        return gates[gateName]

    def __str__(self):
        return f"""inputs: {self.inputs}, weights: {self.weights}, bias: {self.bias}, output: {self.output}
        """



    "__**== Getters and Setters ==**__"
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

# # INVERT gate
# P1 = Perceptron(weights=[-1], bias=0)
# print("INVERT gate",
# P1.calc_output([1]),
# P1.calc_output([0]))
# print(P1)
#
# # AND gate
# P2 = Perceptron(weights=[0.5, 0.5], bias=-1)
# print("AND gate",
# P2.calc_output([0,0]),
# P2.calc_output([0,1]),
# P2.calc_output([1,0]),
# P2.calc_output([1,1]))
# print(P2)
#
# # OR gate
# P3 = Perceptron(weights=[0.5,0.5], bias=-0.5)
# print("OR gate",
# P3.calc_output([0,0]),
# P3.calc_output([0,1]),
# P3.calc_output([1,0]),
# P3.calc_output([1,1]))
# print(P3)
#
# # NOR gate
# P4 = Perceptron(weights=[-1, -1], bias=0)
# print("NOR gate",
# P4.calc_output([0,0]),
# P4.calc_output([0,1]),
# P4.calc_output([1,0]),
# P4.calc_output([1,1]))
# print(P4)
#
# # 3+ input gate
# P5 = Perceptron(weights=[0.6, 0.3, 0.2], bias=-0.4)
# print("3+ input gate",
# P5.calc_output([0, 0, 0]),
# P5.calc_output([0, 0, 1]),
# P5.calc_output([0, 1, 1]),
# P5.calc_output([1, 1, 1]),
# P5.calc_output([1, 0, 0]),
# P5.calc_output([1, 1, 0]),
# P5.calc_output([1, 0, 1]),
# P5.calc_output([1, 1, 1]))
# print(P5)


