import Perceptron as P
from typing import List

class PerceptronLayer:
    layer = None

    def __init__(self, amount: int, gate_names: List[str], n_inputs: int):
        """
        Initializes PerceptronLayer
        :NOTE: The basic weight length is 2, if
        :param amount: The amount of perceptrons in one layer
        :param gate_names: INVERT, AND, OR, NOR, NAND. Gives back perceptron with corresponding weights and bias
        :param n_inputs: the amount of inputs a layer has (not connections but nodes from past layer)
        """
        layer = []
        for i in range(amount):
            try:
                layer.append(P.give_gate(f"{gate_names[i]}", n_inputs))
            except:
                # NAND is given as default perceptron
                layer.append(P.Perceptron(weights=[-1 for i in range(n_inputs)], bias=-1))
        self.layer = layer

    def __str__(self):
        return f"{[[i.weights, i.bias] for i in self.layer]}"

