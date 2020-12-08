import numpy as np
import random
import typing

np.random.seed(3)

class Inputs:
    def __init__(self, inputlist : typing.List[int]):
        self.inputs = inputlist

        self.npinputs = np.array(self.inputs)

    def __getitem__(self, ind : int):
        return self.inputs[ind]

    def setitem(self, ind : int, num : int):
        self.inputs[ind] = num
        self.npinputs = np.array(self.inputs)

    def getList(self) -> typing.List[int]:
        return self.inputs

    @staticmethod
    def calcInputCompliment(s : typing.List[int]) -> typing.List[int]:
        RET = []

        for ind in range(9):
            if s[ind*3 + 2]:
                RET += [0,0,1]

            elif s[ind*3]:
                RET += [0,1,0]

            elif s[ind*3 + 1]:
                RET += [1,0,0]

        return RET

    @staticmethod
    def randInputs() -> str:
        RET = []
        for i in range(9):
            token = [0,0,0]
            token[random.randint(0,2)] = 1

            RET += token

        return RET
