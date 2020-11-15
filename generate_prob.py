#!/usr/bin/python3
"""
Blah blah blah
"""
import numpy as np
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Generates frequency of \
            landing on a square in Monopoly given a prob distrobution of \
            the dice')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dice", action="store", nargs="+",  \
                        help = "List 6 fractions that sum to 1. Each position \
                        corresponds to the probability of the number at \
                        that position+1. e.g. position 0 is the probability \
                        of rolling a 1")
    group.add_argument("--fair", action="count", default = 0, \
                        help = "Flag to use fair dice")
    args = parser.parse_args()
    print(args.fair)


    global DICE_PROB
    if args.fair:
        DICE_PROB = [1/6,1/6,1/6,1/6,1/6,1/6]
    else:
        DICE_PROB = processKWDice(args.dice)


    board = {}
    for i in range(40): #40 sqaures on board, sq 0 is GO
        board[i] = 0

    playerPos = movePlayer(board, 0) #start pos

    for j in range(1000):
        playerPos = movePlayer(board, playerPos)

    print(list(filter(lambda x: x[1]!=0, board.items())))
    print("*"*10)


def movePlayer(board, currentPos):
    """
    Moves the player to the next board sqaure
    @param:
        - board: dict of the board
        - currentPos: where the player is currently located
    @returns: the players position after the dice roll
    """
    if currentPos == 30: #landed on go to jail
        return jail()

    dNum = rollDice()

    nextPos = (dNum + currentPos)%40

    board[nextPos] += 1

    if nextPos in [7,22,36] # chance
        #1/16 nearest utility
            #- pos 12 and 28
        #1/16 st charles (POS 11)
            #-
        # 1/16 jail (POS 10)
        #1/8 go to neartest rail road
            #- POS 5,15,25,35
        #go back 3 spaces
        #go to boardwalk
            #-POS 39
        #go to illoios
            #-POS 24
        # go to GO
            #- POS 0

    if nextPos in [2,17, 33] # community chest
        # 1/16 go to jail (pos 10)
        #1/16 go to GO (pos 0)
        #1/16 reading reail road (POS 5)

    return nextPos


    # if chance:
    #     pass
    # if community chest:
    #     pass

def rollDice():
    """
    Simulates rolling two 6 sided dice. The probability distrobution of the die
    is determined via cmd line
    @param: None
    @returns:  the sum of the two rolls
    """

    global DICE_PROB
    val = [1,2,3,4,5,6]

    try:
        d1 = np.random.choice(val, p=DICE_PROB)
    except:
        print("Probabilities don't sum to 1. Please try again.")
        sys.exit()

    d2 = np.random.choice(val, p=DICE_PROB)

    return (d1+d2)

def processKWDice(lst):
    """
    Processes the dice probabilities from the command line.
    @param list of str
    @return list of floats
    """
    DICE_PROB = []
    for p in lst:
        num, denom = p.split('/')
        n = float(num)/float(denom)
        DICE_PROB.append(float(n))

    if len(DICE_PROB) != 6:
        print("Please input six fractions after the flag.")
        sys.exit()
    return DICE_PROB

def jail():
    """
    Handles moves if you're in jail.
    @returns:
        - 30 if still in jail
        - nextPos if you're out of jail
    """
    # if doubles leave amount of doubles
    # NEED GLOBAL JAIL COUNTER
        #If counter gets to four leave jail and reset

main()
