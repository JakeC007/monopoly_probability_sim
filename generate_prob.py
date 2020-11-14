#!/usr/bin/python3
"""
Blah blah blah
"""

def main():
    #parse arguments here
        # pass in dice probabilities
    #intlz data strctut
    board = {}
    for i in range(40):
        board[i] = 0

    board = movePlayer(board, playerPos)

def movePlayer(board, currentPos):
    pass
    dNum = rollDice()
    nextPos = (dNum + currentPos)%39 # is this 39 or 40?

    if go_to_jail:
        pass
    if chance:
        pass
    if community chest:
        pass

def rollDice():
    pass
    #use num py 
    # todo handle dice probabilities. Gloabl??
