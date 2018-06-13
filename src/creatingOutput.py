import time
import pyautogui
from random import randint

def pick_weak_monster(labeledArray,player):
    monstersNames = ["Goblin", "Zombie", "Warlock", "MeatMan"]
    isMonster = lambda field: type(field).__name__ in monstersNames
    monsters = [field for field in labeledArray if isMonster(field)]

    isWeakMonster = lambda field: player.level >= field.level
    weakMonsters = [field for field in monsters if isWeakMonster(field)]


    #pick random move
    randomMonsterIndex = randint(0,len(weakMonsters)-1)
    return weakMonsters[randomMonsterIndex]

def pickHealField(labeledArray,player):
    #delete fields where you cant move
    unclickableFieldsNames = ["Undiscovered", "wall", "hidden_monster", "hero","Goblin", "Zombie", "Warlock", "MeatMan"]
    isUnclickable = lambda field : type(field).__name__ in unclickableFieldsNames
    possibleMoves = [field for field in labeledArray if not isUnclickable(field)]

    isUndiscovered = lambda field : type(field).__name__ in ["Undiscovered"]
    undiscoveredFields = [field for field in labeledArray if not isUndiscovered(field)]

    nextToUndiscovered = lambda field, table : [(field.positionX == undis.positionX and field.positionY-undis.positionY == 1) or (field.positionY == undis.positionY and field.positionX-undis.positionX == 1) for undis in table]
    for field in possibleMoves:
        if True in nextToUndiscovered(field, undiscoveredFields):
            return field





def pick_move(labeledArray,player):


    if player.currentMonster == None and player.maxHp== 10:
        player.counter = 4
        player.currentMonster = pick_weak_monster(labeledArray,player)
        return player.currentMonster
    elif (not player.currentMonster == None) and not player.counter == 0:
        player.maxHp -= 1
        player.counter -= 1

        return player.currentMonster
    else:
        if not player.healCounter < 3:
            player.healCounter += 1
        else:
            player.healCounter = 0
            player.maxHp = 10
        return pickHealField(labeledArray, player)




def make_move(field):
    x = 249 + (field.positionX+1)*50
    y = 10 + (field.positionY+1)*50

    pyautogui.moveTo(x,y)
    time.sleep(1)
    pyautogui.click(x,y)

def isWon():
    return False