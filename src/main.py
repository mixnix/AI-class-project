#import pyautogui
import time
from PIL import Image
import cv2
import numpy as np
from Fields import *
from Utility import *


def comparePictures(image, template):
    image = np.array(image)
    template = np.array(template)

    img1_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, template_gray, cv2.TM_CCOEFF_NORMED )
    threshold = 0.4
    print(res)
    loc = np.where(res >= threshold)

    #print("Threshold tak jakby: " + str(res))
    for pt in zip(*loc[::-1]):
        #print("p[0] " + str(pt[0]) + " pt[1] " + str(pt[1]))
        if(pt[0] == pt[1]):
            return True
    #print("dlugosc: " + str(len(loc)))
    return False


def createTile(name,x,y):
    tileProducer = {
        #todo: are those tiles, gonna be the same object??? with the same adress
        "undiscovered" : Undiscovered(x,y),
        "altar" : Altar(x,y),
        "empty": Empty(x, y),
        "gold": Gold(x, y),
        "hero": Hero(x, y),
        "hidden_monster": HiddenMonster(x, y),
        "shop": Shop(x, y),
        "wall": Wall(x, y),

    }
    return tileProducer.get(name, DifferentField(x,y))



def classifyTile(tileImg,x,y):
    path = "../res/readyTemplates/"


    #I can make this core prettier by using factory design pattern, then I can streamline
    #differentiating between tiles

    #other category
    otherPath = path + "Other/"
    #undiscovered tile
    otherTileNames = ["undiscovered", "altar", "empty", "gold",
                        "hero", "hidden_monster", "shop", "wall"]
    for name in otherTileNames:
        templateImage = Image.open(otherPath + name + ".png")
        if comparePictures(templateImage, tileImg):
            return createTile(name,x,y)





def classifyGameTiles():
    #load picture
    pic = Image.open("../res/2ndgoblin.png")
    pic.show()

    #slice it into pieces
    list_of_images = slice(pic)

    array_of_tiles = []
    for x in range(len(list_of_images)):
        temp_tiles = []
        for y in range(len(list_of_images[x])):
            temp_tiles.append(classifyTile(list_of_images[x][y], x, y))
        array_of_tiles.append(temp_tiles)

    return array_of_tiles

def testComparePictures():
    oOther = lambda name : Image.open("../res/readyTemplates/Other/" + str(name) + ".png")
    tempDict = {
        #"altar" : oOther("altar"),
        "empty" : oOther("empty"),
        #"gold" : oOther("gold"),
        #"hero" : oOther("hero"),
        #"hidden_monster" : oOther("hidden_monster"),
        #"shop" : oOther("shop"),
        #"undiscovered" : oOther("undiscovered"),
        #"wall" : oOther("wall")
    }

    # for key in tempDict:
    #     tempDict.get(key).show()

    gameBoard = Image.open("../res/initial_screen.png")

    gameBoadPics = slice(gameBoard)


    t = lambda x,y : gameBoadPics[x][y]
    picsDictionary = {
        "altar" : [t(12,0)],
        "empty" : [t(2,0),t(2,2)],
        "gold" : [t(4,17),t(6,18)],
        "hero" : [t(6,2)],
        "hidden_monster" : [t(16,8),t(16,14)],
        "shop" : [t(2,1),t(8,6)],
        #"undiscovered" : [t(0,0),t(8,0),t(0,5),t(13,15)],
        "wall" : [t(1,0),t(0,1),t(1,1)],
    }

    # for key in picsDictionary:
    #     for l in range(len(picsDictionary.get(key))):
    #         picsDictionary.get(key)[l].show()

    for picKey in picsDictionary:
        for pic in picsDictionary.get(picKey):
            for keyTemp in tempDict:
                if(picKey == keyTemp):
                    match = True
                else:
                    match = False
                pic.show()
                tempPic = tempDict.get(keyTemp)
                tempPic.show()
                comparison = comparePictures(pic, tempPic)
                print(comparison)
                #assert comparison == match


    #todo: do all these tests, use assert to do this



    # pic of empty 1 up
    emptyPic = gameBoadPics[1][3]



    wallPic = gameBoadPics[1][3]



    #template of empty field
    undiscoveredTemplate = Image.open("../res/readyTemplates/Other/undiscovered.png")
    # undiscoveredTemplate.show()



    #template matching
    #assert(not comparePictures(wallPic, undiscoveredTemplate))


testComparePictures()
    #firstly test if templates compared to picture is true, really many test cases
    #figure out how to partially automate it, for example make image field in class and test
    # if class is the same


    # #final test if classifying whole board will work
    # array_of_tiles = classifyGameTiles()
    # for x in range(len(array_of_tiles)):
    #     for y in range(len(array_of_tiles[x])):
    #         print(array_of_tiles[y][x],end="")
    #     print()



