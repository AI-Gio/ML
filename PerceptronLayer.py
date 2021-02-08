import Perceptron as P

class PerceptronLayer:
    layer = None

    def __init__(self, amount, gateNames, n_inputs):
        """
        Initializes PerceptronLayer
        :NOTE: The basic weight length is 2, if
        :param amount: The amount of perceptrons in one layer
        :param gateNames: INVERT, AND, OR, NOR, NAND. Gives back perceptron with corresponding weights and bias
        """
        layer = []
        p = P.Perceptron(weights=[], bias=0)
        for i in range(amount):
            try:
                layer.append(p.give_gate(f"{gateNames[i]}", n_inputs))
            except:
                # NAND is given as default perceptron
                layer.append(P.Perceptron(weights=[-1 for i in range(n_inputs)], bias=-1))
        self.layer = layer

    def __str__(self):
        return f"{[[i.weights, i.bias] for i in self.layer]}"
