from PIL import Image
from Comparing import *
from Fields import *
from Utility import *
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


def testCreateFields():
    pustePole = Empty(1,2)
    print(pustePole)

def runTests():
    testCreateFields()
    testComparePictures()