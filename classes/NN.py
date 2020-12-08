import numpy as np
import funcs
from classes.Inputs import Inputs
"""
27 binary inputs
2 hidden layers
9 binary output layer with softmax

input (27) h1 (9) h2 (9) out
"""

np.random.seed(3)

class NN:
    def __init__(self, w = None):
        if w == None:
            self.weights = NN.randWeights()
        else:
            self.weights = w

    def _prop(self, inputs : Inputs):
        forward = [np.array(inputs.inputs)]

        # do hidden layers
        for ind in range(2):
            forward.append(np.dot(forward[-1], self.weights[ind]))
            forward[-1] = funcs.ReLU(forward[-1])

        # do output layer
        forward.append(funcs.sigmoid(forward[-1]))

        # softmax the output
        output = forward[-1]
        output = funcs.softmax(output)

        return output

    def choice(self, inputs : Inputs) -> int:
        output = self._prop(inputs)

        # maps the indexs to the values
        indout = [(ind, output[ind]) for ind in range(9)]
        indout.sort(key=NN._comp)

        # sorts so biggest is first
        indout = indout[::-1]

        boardin = inputs.inputs
        # print(indout)

        # '000' = (i moved, he moved, empty)
        for (move, prob) in indout:
            if boardin[3 * move + 2] == 1:
                return move

        # there will always be a valid move
        # if not then resign
        return -1

    def getWeights(self):
        return self.weights

    @staticmethod
    def randWeights ():
        return [np.random.rand(27,9),
                np.random.rand(9,9),
                np.random.rand(9,9)]

    @staticmethod
    def _comp (x):
        return x[1]
