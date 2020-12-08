# there are 3^9 games
# length of 9

from classes.Inputs import Inputs
from classes.Player import Player
from classes.NN import NN
from classes.Board import Board
import numpy as np
import random
from random import randint

# create 100 players
# for every round pair them up and get the victor
# those with higher fitness will then breed
# and also mutate

players = [Player(NN.randWeights(), 0.5) for _ in range(100)]
games = []

def comp(x):
    return x.score

for _ in range(30):
    print(_)
    random.shuffle(players)

    games = [Board(players[2*i], players[2*i+1]) for i in range(len(players)//2)]
    winners = []

    for i in range(len(players)//2):
        winners.append(games[i].play())

    maxscore = 0

    for i in range(len(players)//2):
        if winners[i] == -1:
            continue

        # print(winners[i])
        maxscore = max(winners[i].score, maxscore)
        winners[i].score += 2

    winners.sort(key=comp)
    winners = winners[::-1]

    newplayers = winners + players

    for _ in range(max(0, winners[0].score)):
        newplayers.append(winners[0].mutate())

    random.shuffle(newplayers)
    # keep it at length 100
    if len(newplayers) > 100:
        newplayers = newplayers[:100]

    # # cross breed
    # for i in range(randint(0,len(newplayers))):
    #     Player.crossbreed(newplayers[i], newplayers[randint(0,99)])

    players = newplayers

    if len(players) < 100:
        for i in range(100 - len(players)):
            players.append(winners[0])

    print(maxscore)

print(players[0].score)
print(players[0].getWeights())
