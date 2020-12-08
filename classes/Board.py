import numpy as np
from classes.Inputs import Inputs
from classes.NN import NN
from classes.Player import Player
from random import randint
import typing

_precompute = []
for _ in range(9):
    _precompute += [0,0,1]

class Board:
    emptyBoard = _precompute

    def __init__(self, p1 : Player, p2 : Player):
        self.board = Board.emptyBoard
        self.p1 = p1 # will be X
        self.p2 = p2 # will be O

        self.turn = randint(0,1) # player 1 or player 2 starts

    def play(self) -> Player: # returns the winning player
        # the two game strings will be compliments

        while not Board.checkWin(self.board):

            if self.turn == 0:
                currmove = self.p1.getMove(Inputs(self.board))

            else:
                currmove = self.p2.getMove(Inputs(Inputs.calcInputCompliment(self.board)))

            #check if one resigned
            if currmove == -1:
                # check if the board is full
                if Board.checkBoardFull(self.board):
                    return None

                else:
                    if self.turn == 0:
                        return self.p2
                    elif self.turn == 1:
                        return self.p1

            #change the board to fit the move
            self.board[currmove * 3 + self.turn] = 1
            self.board[currmove * 3 + 2] = 0

            self.turn = (self.turn + 1) % 2 # flips the turn

            # print(np.array(Board.conv2d(self.board)),'\n')

        if self.turn == 0:
            return self.p1
        else:
            return self.p2

    @staticmethod
    def conv2d(board : typing.List[int]) -> typing.List[str]:
        d2board = [[None for _ in range(3)] for _ in range(3)]

        #fill it
        for i in range(3):
            if board[i*3] == 1:
                d2board[0][i] = 'X'
            elif board[i*3 + 1] == 1:
                d2board[0][i] = 'O'
            else:
                d2board[0][i] = ' '

        for i in range(3):
            for j in range(3):
                if board[i*9 + j*3] == 1:
                    d2board[i][j] = 'X'

                elif board[i*9 + j*3 + 1] == 1:
                    d2board[i][j] = 'O'

                else:
                    d2board[i][j] = ' '

        return d2board

    @staticmethod
    def checkWin(board : typing.List[int]) -> bool:
        d2board = Board.conv2d(board)

        # check the rows
        for rowind in range(3):
            tempset = set()
            for i in range(3):
                tempset.add(d2board[rowind][i])

            if len(tempset) == 1 and ('X' in tempset or 'O' in tempset):
                return True

        #check the cols
        for colind in range(3):
            tempset = set()
            for i in range(3):
                tempset.add(d2board[i][colind])

            if len(tempset) == 1 and ('X' in tempset or 'O' in tempset):
                return True

        #check the diamonds
        tempset = set()
        tempset2 = set()
        for o in range(3):
            tempset.add(d2board[o][o])
            tempset2.add(d2board[2-o][o])

        if len(tempset) == 1 and ('X' in tempset or 'O' in tempset):
            return True

        if len(tempset2) == 1 and ('X' in tempset or 'O' in tempset):
            return True

        return False

    @staticmethod
    def checkBoardFull(board: Inputs) -> bool:
        for i in range(9):
            if board[i*3 + 2] == 1:
                return True

        return False
