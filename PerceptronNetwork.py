import PerceptronLayer as pl
from typing import List

class PerceptronNetwork:
    network = []
    bit_pos = None

    def __init__(self, inputs: int, structure: list):
        network = []
        for layer in structure:
            network.append(pl.PerceptronLayer(layer[0], layer[1], layer[2]))
        self.network = network
        self.inputs = inputs

    def feed_forward(self, inputs: List[int]) -> List[List[int]]:
        """
        Gives back the outputs from perceptron network, given the amount of nodes within the input layer.
        :param inputs: A list with an input. Ex. : [0, 0, 1]
        :return: A list with for each input possibility the output
        """
        new_inputs = inputs
        # loops through the layers of the network
        for layer in self.network:
            output = []
            # loops through the perceptrons of the layer
            for perceptron in layer.layer:
                output.append(perceptron.calc_output(new_inputs))
            new_inputs = output
        return new_inputs

    def __str__(self):
        la = 0
        for l in self.network:
            la += 1
            print(f"Layer #{la}")
            for p in range(len(l.layer)):
                for w in l.layer[p].get_weights():
                    print(f"input * {w} + {l.layer[p].get_bias()}")
        return ""

def per(n: int) -> List[List[int]]: # bron: https://stackoverflow.com/questions/14931769/how-to-get-all-combination-of-n-binary-value
    """
    Creates map with all of the bit possibilities
    :param n: bit places amount
    :return: map with all of the bit possibilities
    """
    pos = []
    for i in range(1 << n):
        s = bin(i)[2:]
        s = '0' * (n - len(s)) + s
        pos.append(list(map(int, list(s))))
    return pos



