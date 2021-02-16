from typing import List, Union

class Perceptron:
    inputs = None
    output = None

    def __init__(self, weights: List[Union[float, int]], bias: Union[float, int]):
        """
        Initializes perceptron with needed attributes
        :param weights: list of weights (inputwise) (order of the elements should correspond with the order of inputs)
        :param bias: integer that stands for the bias
        """
        self.weights = weights
        self.bias = bias

    def calc_output(self, inputs: List[int]) -> int:
        """
        Calculates the output of the perceptron using the input values and corresponding weights and the bias
        to compare with the threshold
        :param inputs: a list with 0's and 1's
        :return: Boolean value
        """
        if len(inputs) != len(self.weights):
            raise ValueError("The amount of inputs and the amount of weights do not correspond")

        # multiplies input values with corresponding weights
        paths = [a * b for a, b in zip(inputs, self.weights)]
        # output gets a bitwise value by converting a boolean expression into an integer
        self.output = int((self.bias + sum(paths)) >= 0)
        self.inputs = inputs
        return self.output


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

def give_gate(gate_name: str, n_inputs: int) -> Perceptron:
    """
    Takes the amount of inputs and specifies what preset node to take
    :param gate_name: A list with string that contain gate names
    :param n_inputs: how many inputs a gate has
    :return: a Perceptron with the correct weights and bias
    """
    gates = {
    "INVERT": Perceptron(weights=[-1], bias=0),
    "AND": Perceptron(weights=[0.5 for i in range(n_inputs)], bias=n_inputs * -0.5),
    "OR": Perceptron(weights=[0.5 for i in range(n_inputs)], bias=-0.5),
    "NOR": Perceptron(weights=[-1 for i in range(n_inputs)], bias=0),
    "NAND": Perceptron(weights=[-1 for i in range(n_inputs)], bias=n_inputs-1)
    }
    return gates[gate_name]