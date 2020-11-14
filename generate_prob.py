#!/usr/bin/python3
"""
Blah blah blah
"""
import numpy as np
import argparse
import sys

def main():
    #parse arguments here
        # pass in dice probabilities
    #intlz data strctut
    parser = argparse.ArgumentParser(description='Generates frequency of \
            landing on a square in Monopoly given a prob distrobution of \
            the dice')
    parser.add_argument("--dice", action="store", nargs="+",  \
                        help = "List 6 fractions that sum to 1. Each position \
                        corresponds to the probability of the number at \
                        that position+1. e.g. position 0 is the probability \
                        of rolling a 1")
    parser.add_argument("--fair", action="count", default = 0, \
                        help = "Flag to use fair dice")
    args = parser.parse_args()
    print(args.fair)


    global DICE_PROB
    if args.fair:
        DICE_PROB = [1/6,1/6,1/6,1/6,1/6,1/6]
    else:
        DICE_PROB = []
        for p in args.dice:
            num, denom = p.split('/')
            n = float(num)/float(denom)
            DICE_PROB.append(float(n))
        if sum(DICE_PROB) != 1:
            print("Probabilities don't sum to 1. Please try again.")
            sys.exit()
        if len(DICE_PROB) != 6:
            print("Please input six fractions after the flag.")
            sys.exit()

    board = {}
    for i in range(40): #40 sqaures on board, sq 0 is GO
        board[i] = 0

    playerPos = movePlayer(board, 0) #start pos

    for j in range(1000):
        playerPos = movePlayer(board, playerPos)

    print(list(filter(lambda x: x[1]!=0, board.items())))
    print("*"*10)


def movePlayer(board, currentPos):
    dNum = rollDice()

    nextPos = (dNum + currentPos)%40

    board[nextPos] += 1

    return nextPos

    # if go_to_jail:
    #     pass
    # if chance:
    #     pass
    # if community chest:
    #     pass

def rollDice():
    global DICE_PROB
    val = [1,2,3,4,5,6]
    d1 = np.random.choice(val, p=DICE_PROB)
    d2 = np.random.choice(val, p=DICE_PROB)
    return (d1+d2)

main()
