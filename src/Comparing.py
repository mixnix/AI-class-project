from Fields import *
import numpy as np

from PIL import Image
import cv2



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

def compareWithThreshold(image, template, thresholdArg):
    image = np.array(image)
    template = np.array(template)

    img1_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, template_gray, cv2.TM_CCOEFF_NORMED )
    threshold = thresholdArg
    #print(res)
    loc = np.where(res >= threshold)

    #print("Threshold tak jakby: " + str(res))
    for pt in zip(*loc[::-1]):
        #print("p[0] " + str(pt[0]) + " pt[1] " + str(pt[1]))
        if(pt[0] == pt[1]):
            return True
    #print("dlugosc: " + str(len(loc)))
    return False


def comparePicturesRetThreshold(image, template):
    image = np.array(image)
    template = np.array(template)

    img1_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, template_gray, cv2.TM_CCOEFF_NORMED )
    threshold = 0.4
    return res[0][0]