import time
import pyautogui
from random import randint


def pick_move(labeledArray):
    #delete fields where you cant move
    unclickableFieldsNames = ["Undiscovered", "wall", "hidden_monster", "hero"]
    isUnclickable = lambda field : type(field).__name__ in unclickableFieldsNames
    possibleMoves = [field for field in labeledArray if not isUnclickable(field)]

    #pick random move
    randomFieldIndex = randint(0,len(possibleMoves)-1)
    return possibleMoves[randomFieldIndex]


def make_move(field):
    x = 259 + (field.positionX+1)*48
    y = 10 + (field.positionY+1)*48

    pyautogui.moveTo(x,y)
    time.sleep(1)
    pyautogui.click(x,y)

def isWon():
    return False