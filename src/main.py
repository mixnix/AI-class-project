import pyautogui
import time
from PIL import Image
import cv2
import numpy as np

def slice(img):
    slicesX = 20
    slicesY = 20

    left = 260

    #constants that in future should be generated automatically by detecting edges and calculating
    slice_sizeX = 50
    slice_sizeY = 50

    countX = 1

    list_to_be_returned = []

    for X in range(slicesX):
        right = left + slice_sizeX

        temp_list = []

        upper = 30
        countY = 1
        for Y in range(slicesY):
            lower = upper + slice_sizeY

            equalizer = 2
            bbox = (left+equalizer, upper+equalizer, right+equalizer, lower+equalizer)
            working_slice = img.crop(bbox)
            upper += slice_sizeY

            temp_list.append(working_slice)

            countY += 1

        left += slice_sizeX
        countX += 1
        list_to_be_returned.append(temp_list)
    return list_to_be_returned

def comparePictures(image, template):
    image = np.array(image)
    template = np.array(template)
    img1_gray = image #cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    img2_gray = template#cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF )
    threshold = 0.9
    loc = np.where(res >= threshold)

    #print("Threshold tak jakby: " + str(res))
    for pt in zip(*loc[::-1]):
        #print("p[0] " + str(pt[0]) + " pt[1] " + str(pt[1]))
        if(pt[0] == pt[1]):
            return True
    #print("dlugosc: " + str(len(loc)))
    return False

class Field:
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y

class DifferentField(Field):
    def __str__(self):
        return "d "

class Undiscovered(Field):
    def __str__(self):
        return "u "

class Altar(Field):
    def __str__(self):
        return "a "

class Empty(Field):
    def __str__(self):
        return "e "

class Gold(Field):
    def __str__(self):
        return "g "

class Hero(Field):
    def __str__(self):
        return "h "

class HiddenMonster(Field):
    def __str__(self):
        return "hm "

class Shop(Field):
    def __str__(self):
        return "a "

class Wall(Field):
    def __str__(self):
        return "w "

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
    gameBoard = Image.open("../res/initial_screen.png")

    gameBoadPics = slice(gameBoard)

    #picture of wall
    wallPic = gameBoadPics[1][3]
    #wallPic.show()

    #template of empty field
    undiscoveredTemplate = Image.open("../res/readyTemplates/Other/undiscovered.png")
   # undiscoveredTemplate.show()

    #template matching
    print(comparePictures(wallPic, undiscoveredTemplate))

if __name__ == '__main__':
    # #firstCompareTest()
    # array_of_tiles = classifyGameTiles()
    # for x in range(len(array_of_tiles)):
    #     for y in range(len(array_of_tiles[x])):
    #         print(array_of_tiles[y][x],end="")
    #     print()
    testComparePictures()