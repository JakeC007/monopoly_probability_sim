#!/usr/bin/python3
"""
Blah blah blah
"""
import numpy as np
import random
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

    global jailCnt
    jailCnt = 0

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

    if nextPos in [7,22,36]: # chance squares
        nextPos = chance_c(nextPos)

    if nextPos in [2,17, 33]: # community chest squares
        nextPos = community_chest()

    return nextPos

def rollDice(jail=False):
    """
    Simulates rolling two 6 sided dice. The probability distrobution of the die
    is determined via cmd line
    @param: None
    @returns:
        - the sum of the two rolls if not in jail
        - the value of both rolls if in jail
    """

    global DICE_PROB
    val = [1,2,3,4,5,6]

    try:
        d1 = np.random.choice(val, p=DICE_PROB)
    except:
        print("Probabilities don't sum to 1. Please try again.")
        sys.exit()

    d2 = np.random.choice(val, p=DICE_PROB)

    if jail == True:
        return d1, d2
    else:
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
    Handles moves if you're in jail. A player can leave jail if (1) they roll
    doubles or (2) it is their third turn in jail
    @returns:
        - 30 if still in jail
        - nextPos if you're out of jail
    """
    global jailCnt
    jailCnt += 1

    if jailCnt == 4: # leave jail; end of 3 turn stay
        jailCnt = 0
        return (10 + rollDice())
    else:
        d1, d2 = rollDice(True)
        if d1 == d2: # roll doubles; leave jail
            jailCnt = 0
            return (10 + d1 + d2)
        else: # stuck in jail
            return 30

def community_chest():
    """
    Simulates pulling a community chest card. The cards have the following
    operations on movement:
        - move to jail (pos 10)
        - move to GO (pos 0)
        -move to reading railroad (pos 5)
    @param: None
    @ret: new position of player
    """
    chestCards = [10,0,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    return random.choice(chestCards)

def chance_c(currentPos):
    """
    """
    chanceDeck = {
                "nearestUtility": nearestUtility,
                "moveSt_charles": 11,
                "jail": 30,
                "nearestRail": nearestRail,
                "backThree": backThree,
                "moveBoardwalk": 39,
                "moveIllinois": 24,
                "moveGO": 0,
                "NOTHING": -1
            }
    cards =  list(chanceDeck.keys())
    d = np.random.choice(cards, p=[1/16,1/16,1/16,1/8,1/16,1/16,1/16,1/16,7/16])
    print(f"doing {d}, current position {currentPos}")
    try:
        ret = chanceDeck[d](currentPos)
    except:
        ret = chanceDeck[d]
        if ret == -1:
            ret = currentPos
    print(f"new position is {ret}")
    return ret

def nearestUtility(currentPos):
    """
    Moves the player to the nearest utility
        - either pos 12 or 28
    @param: player's current position
    @returns player's new position
    """
    if currentPos > 12 and currentPos <= 28:
        return 28
    else:
        return 12

def nearestRail(currentPos):
    """
    Moves the player to the nearest utility
        - either pos 5, 15, 25, or 35
    @param: player's current position
    @returns player's new position
    """
    for i in [5,15,25,35]:
        delta = i - currentPos
        if delta > 0:
            return i

    return 5 # player is past sq. 35; sq. 5 is now the closest

def backThree(currentPos):
    """
    Moves the player back three spaces
    @param: player's current position
    @returns player's new position
    """
    return (currentPos - 3)%40

main()
