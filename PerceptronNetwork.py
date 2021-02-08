import PerceptronLayer as pl

class PerceptronNetwork:
    network = []
    bit_pos = None

    def __init__(self, inputs, structure):
        network = []
        for layer in structure:
            network.append(pl.PerceptronLayer(layer[0], layer[1], layer[2]))
        self.network = network
        self.inputs = inputs

    def per(self, n):
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


    def feed_forward(self):
        """
        Gives back the outputs from perceptron network, given the amount of nodes within the input layer.
        :param inputs: amount of input nodes (integer)
        :return: A list with for each input possibility the output
        """
        bit_pos = self.per(self.inputs)
        result = []
        # loops through possible inputs
        for pos in bit_pos:
            new_inputs = pos
            # loops through the layers of the network
            for layer in self.network:
                outputs = []
                # loops through the perceptrons of the layer
                for perceptron in layer.layer:
                    outputs.append(perceptron.calc_output(new_inputs))
                new_inputs = outputs
            result.append(new_inputs)
        self.bit_pos = bit_pos
        return result

    def __str__(self):
        print("Results:")
        output = self.feed_forward()
        for c, pos in enumerate(self.bit_pos):
            print(f"{pos}   {output[c]}")

        la = 0
        for l in self.network:
            la += 1
            print(f"Layer #{la}")
            for p in range(len(l.layer)):
                for w in l.layer[p].get_weights():
                    print(f"input * {w} + {l.layer[p].get_bias()}")
        return ""

# XOR gate
xor = PerceptronNetwork(2, [[2, ["NAND", "OR"],2], [1, ["AND"], 2]])
print(xor)


# Half adder Gate
# Built up structure
PN1 = PerceptronNetwork(2, [[3,["NAND", "OR", "AND"], 2], [2,["AND"], 3]])
# Change default weights to correct weights
PN1.network[1].layer[0].set_weights(weights=[0.5, 0.5, 0])
PN1.network[1].layer[1].set_weights(weights=[0, 0 ,1])
print(f"Bias last layer, 1nd node: {PN1.network[1].layer[0].get_bias()}")
print(f"Bias last layer, 2nd node: {PN1.network[1].layer[1].get_bias()}")
# Change calculated bias to correct bias
PN1.network[1].layer[0].set_bias(-1)
PN1.network[1].layer[1].set_bias(-1)
print(PN1)


