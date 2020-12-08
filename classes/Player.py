import numpy as np
from classes.Inputs import Inputs
from classes.NN import NN
import random

"""
genetic material : list = weights
mutation rate : int
"""

# this could be an inherited class but I don't care
class Player:
    def __init__(self, w, mrate : float):
        self.nn = NN(w)
        self.mrate = mrate
        self.mscale = 3.14
        self.score = 0

    def getWeights(self):
        return self.nn.getWeights()

    def getNN(self):
        return self.nn

    def getMove(self, inputs : Inputs):
        return self.nn.choice(inputs)

    def mutate(self):
        RET = self

        for i in range(27):
            for j in range(9):
                if (random.random() < self.mrate):
                    r = random.randint(0,1)

                    if r:
                        RET.nn.weights[0][i][j] += self.mscale
                    else:
                        RET.nn.weights[0][i][j] -= self.mscale

        for i in range(9):
            for j in range(9):
                if (random.random() < self.mrate):
                    r = random.randint(0,1)

                    if r:
                        RET.nn.weights[1][i][j] += self.mscale
                    else:
                        RET.nn.weights[1][i][j] -= self.mscale

        for i in range(9):
            for j in range(9):
                if (random.random() < self.mrate):
                    r = random.randint(0,1)

                    if r:
                        RET.nn.weights[2][i][j] += self.mscale
                    else:
                        RET.nn.weights[2][i][j] -= self.mscale

        return RET

    @staticmethod
    def crossbreed(p1, p2):
        pass
