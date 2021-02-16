import unittest
import Perceptron as p
import PerceptronNetwork as pn

class MyTestCase(unittest.TestCase):
    def test_P_INVERT(self):
        invert = p.give_gate("INVERT", 1)
        pos = pn.per(1)
        output = []
        for x in pos:
            output.append(invert.calc_output(x))
        self.assertEqual(output, [1,0])

    def test_P_AND(self):
        AND = p.give_gate("AND", 2)
        pos = pn.per(2)
        output = []
        for x in pos:
            output.append(AND.calc_output(x))
        self.assertEqual(output, [0,0,0,1])

    def test_P_OR(self):
        OR = p.give_gate("OR", 2)
        pos = pn.per(2)
        output = []
        for x in pos:
            output.append(OR.calc_output(x))
        self.assertEqual(output, [0,1,1,1])

    def test_P_NOR(self):
        NOR = p.give_gate("NOR", 3)
        pos = pn.per(3)
        output = []
        for x in pos:
            output.append(NOR.calc_output(x))
        self.assertEqual(output, [1,0,0,0,0,0,0,0])

    def test_P_PARTY(self):
        PARTY = p.Perceptron(weights=[0.6, 0.3, 0.2], bias=-0.4)
        pos = pn.per(3)
        output = []
        for x in pos:
            output.append(PARTY.calc_output(x))
        self.assertEqual(output, [0,0,0,1,1,1,1,1])

    def test_PN_XOR(self):
        XOR = pn.PerceptronNetwork(2, [[2, ["NAND", "OR"],2], [1, ["AND"], 2]])
        pos = pn.per(2)
        output = []
        for x in pos:
            output.append(XOR.feed_forward(x))
        self.assertEqual(output, [[0],
                                  [1],
                                  [1],
                                  [0]])

    def test_PN_half_adder(self):
        ha = pn.PerceptronNetwork(2, [[3,["NAND", "OR", "AND"], 2], [2,["AND"], 3]])
        ha.network[1].layer[0].set_weights(weights=[0.5, 0.5, 0])
        ha.network[1].layer[1].set_weights(weights=[0, 0, 1])
        ha.network[1].layer[0].set_bias(-1)
        ha.network[1].layer[1].set_bias(-1)
        pos = pn.per(2)
        output = []
        for x in pos:
            output.append(ha.feed_forward(x))
        self.assertEqual(output, [[0,0],
                                  [1,0],
                                  [1,0],
                                  [0,1]])


if __name__ == '__main__':
    unittest.main()


