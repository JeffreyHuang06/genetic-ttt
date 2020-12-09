from classes.Board import Board
from classes.Inputs import Inputs
from classes.NN import NN
from classes.Player import Player
import numpy as np
import funcs

with open("bestoutof30","r+") as fin:
    raw = [i.rstrip('\n') for i in fin.readlines()]

w_1 = raw[:81]
w_1_str = ""
for i in w_1:
    w_1_str += i

exec(f"w_1 = np.array({w_1_str})")

w_2 = raw[82:109]
w_2_str = ""
for i in w_2:
    w_2_str += i

exec(f"w_2 = np.array({w_2_str})")

w_3 = raw[110:137]
w_3_str = ""
for i in w_3:
    w_3_str += i

exec(f"w_3 = np.array({w_3_str})")

weights = [w_1, w_2, w_3]

player = Player(weights, 0.5)

board = Board.emptyBoard

def parseIn(x : int):
    global board
    board[3*x + 2] = 0
    board[3*x] = 1

def parseHim(x : int):
    global board
    board[3*x + 2] = 0
    board[3*x + 1] = 1

while(1):
    inp = int(input())

    parseIn(inp)

    nmove = player.getMove(Inputs(Inputs.calcInputCompliment(board)))
    parseHim(nmove)

    print(np.array(Board.conv2d(board)) , '\n')
