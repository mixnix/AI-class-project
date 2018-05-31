from PIL import Image
from Comparing import *
from Fields import *
from Utility import *
from structures.TempTest import *

def loadDictionaries():
    oOther = lambda name, friendClasses: TempTest(Image.open("../res/readyTemplates/Other/" + str(name) + ".png"),
                                                  friendClasses, name)
    oMeat = lambda name, friendClasses : TempTest(Image.open("../res/readyTemplates/Monsters/MeatMan/" + str(name) + ".png"),
                                                  friendClasses, name)
    oGoblin = lambda name, friendClasses: TempTest(
        Image.open("../res/readyTemplates/Monsters/Goblin/" + str(name) + ".png"),
        friendClasses, name)
    oWarlock = lambda name, friendClasses: TempTest(
        Image.open("../res/readyTemplates/Monsters/Warlock/" + str(name) + ".png"),
        friendClasses, name)
    oZombie = lambda name, friendClasses: TempTest(
        Image.open("../res/readyTemplates/Monsters/Zombie/" + str(name) + ".png"),
        friendClasses, name)

    tempDict = {
        "altar": oOther("altar", []),
        "blood": oOther("blood", []),
        #"bonusatk": oOther("bonusatk", ["bonushp", "bonusmp"]),
        #"bonushp": oOther("bonushp", ["bonusatk", "bonusmp"]),
        #"bonusmp": oOther("bonusmp", ["bonushp", "bonusatk"]),
        "empty": oOther("empty", []),
        "gold": oOther("gold", []),
        "hero": oOther("hero", []),
        "hidden_monster": oOther("hidden_monster", []),
        "hppotion": oOther("hppotion", []),
        "shop": oOther("shop", []),
        # "undiscovered" : oOther("undiscovered",[]),
        "wall": oOther("wall", []),
        #"wonafyt" : oOther("wonafyt",[]), #spell
        #"burndayraz" : oOther("burndayraz",[]),  #spell
        #"bysspes" : oOther("bysspes",[]), #spell
        #"getindare" : oOther("getindare",[]), #spell
        #"imawal" : oOther("imawal",[]), #spell
        #"lemmisi" : oOther("lemmisi",[]), #spell
        #"mppotion" : oOther("mppotion",[]), #other potion
        #"pisorf" : oOther("pisorf",["tele"]), #spell
        #"tele" : oOther("tele",["pisorf"]), #spell
        #"waldes" : oOther("waldes",[]), #spell

        "Goblin" : oGoblin("4",[]),
        #"MeatMan" : oMeat("1",[]),
        "Warlock" : oWarlock("1", []),
        "Zombie" : oZombie("3",[])

    }
    gameBoard1 = Image.open("../res/initial_screen.png")
    gameBoadPics1 = slice(gameBoard1)
    t = lambda x, y: gameBoadPics1[x][y]

    gameBoard2 = Image.open("../res/2.png")
    gameBoadPics2 = slice(gameBoard2)
    u = lambda x, y: gameBoadPics2[x][y]

    gameBoard3 = Image.open("../res/full_print_screen.png")
    gameBoadPics3 = slice(gameBoard3)
    v = lambda x, y: gameBoadPics3[x][y]

    gameBoard4 = Image.open("../res/summonmonster.png")
    gameBoadPics4 = slice(gameBoard4)
    uu = lambda x, y: gameBoadPics4[x][y]

    gameBoard5 = Image.open("../res/lemmisee.png")
    gameBoadPics5 = slice(gameBoard5)
    uv = lambda x, y: gameBoadPics5[x][y]

    gameBoard6 = Image.open("../res/destroywall.png")
    gameBoadPics6 = slice(gameBoard6)
    ut = lambda x, y: gameBoadPics6[x][y]

    # 11, 14
    picsDictionary = {
        "altar": [t(12, 0), v(8, 0)],
        "blood": [u(6, 15), u(11, 16), u(14, 15)],
        "bonusatk": [u(8, 5), u(14, 6)],
        "bonushp": [u(2, 4), v(6, 2)],
        "bonusmp": [u(5, 4), v(11, 8)],
        "empty": [t(2, 0), t(2, 2)],
        "gold": [t(4, 17), t(6, 18)],
        "hero": [t(6, 2), u(7, 12)],
        "hidden_monster": [t(16, 8), t(16, 14)],
        "hppotion": [u(14, 1), u(14, 8)],
        "shop": [t(2, 1), t(8, 6)],
        #"undiscovered": [t(0, 0), t(8, 0), t(0, 5), t(13, 15)],
        "wall": [t(1, 0), t(0, 1), t(1, 1)],
        # "burndayraz": [u(8, 9), v(10, 17)],  # spell
        # "bysspes": [u(16, 19), uu(8, 10)],  # spell
        # "getindare": [u(16, 10), v(16, 14)],  # spell
        # "imawal": [u(10, 3), v(10, 16)],  # spell
        # "lemmisi": [uv(9, 9)],  # spell
        # "mppotion": [u(16, 9), u(17, 11)],  # other potion
        # "pisorf": [t(11,12)],  # spell
        # "tele": [v(6, 5), uu(8, 11)],  # spell
        # "wonafyt": [v(7, 8), uu(8, 8),v(7, 8)],  # spell
        # "waldes": [ut(11, 14)],  # spell

        "Goblin": [t(2,4),t(8,7)],
        "MeatMan": [t(4,2),t(1,8)], #lvl 4 and 7
        "Warlock": [t(0,2), t(6,6)], #lvl 8 and 2
        "Zombie": [t(6,3),t(14,4)], #lvl 3 and 4

    }
    return picsDictionary, tempDict



def findThresholds2(tempDict, picsDictionary):
    #show best threshold for each template

    varThresholdDetectionPossible = True
    contThresholdDetectionPossible = True

    absoluteMinRightThreshold = 1
    absoluteMaxWrongThreshold = 0
    for keyTemp in tempDict:
        minRightThreshold = 1
        maxWrongThreshold = 0
        for picKey in picsDictionary:
            for pic in picsDictionary.get(picKey):
                tempObject = tempDict.get(keyTemp)
                tempPic = tempObject.img

                similarity = comparePicturesRetThreshold(pic, tempPic)
                if(picKey == keyTemp):
                    if(similarity < minRightThreshold):
                        minRightThreshold = similarity
                elif(not tempObject.friendClasses.__contains__(picKey)):  #jak sprawdzic zawieranie sie w tablicy
                    if(similarity > maxWrongThreshold):
                        maxWrongThreshold = similarity
        tempDict.get(keyTemp).threshold = minRightThreshold
        if(minRightThreshold < absoluteMinRightThreshold):
            absoluteMinRightThreshold = minRightThreshold
        if(maxWrongThreshold > absoluteMaxWrongThreshold):
            absoluteMaxWrongThreshold = maxWrongThreshold
        # print("Key: " + keyTemp)
        # print("minimum right threshold = " + str(minRightThreshold))
        # print("maximum wrong threshold = " + str(maxWrongThreshold))
        # print()
        if(minRightThreshold < maxWrongThreshold):
            varThresholdDetectionPossible = False

    if(absoluteMinRightThreshold < absoluteMaxWrongThreshold):
        contThresholdDetectionPossible = False

    print("Constant threshold template matching possible?: " + str(contThresholdDetectionPossible))
    print("Variable threshold template matching possible?: " + str(varThresholdDetectionPossible))
    return  tempDict

def testCompareAll(tempDict, picsDictionary):

    for picKey in picsDictionary:
        for pic in picsDictionary.get(picKey):
            for keyTemp in tempDict:

                if(picKey == keyTemp):
                    match = True
                else:
                    match = False
                #pic.show()
                print(picKey + " == " + keyTemp + " ?")
                tempObject = tempDict.get(keyTemp)
                #tempPic.show()
                comparison = compareWithThreshold(pic, tempObject.img, tempObject.threshold)
                print(comparison)
                if(picKey == keyTemp):
                    assert comparison
                elif(not tempObject.friendClasses.__contains__(picKey)):
                    assert not comparison
                #assert comparison == match
                print()

def testColor(picsDictionary,color,colorStr):
    for picKey in picsDictionary:
        for pic in picsDictionary.get(picKey):
            black = 0
            for pixel in pic.getdata():
                if pixel == color:
                    black += 1
            print(picKey + ' ma: ' + str(black) + " pixeli " + colorStr)

def countColorPixels(picArray, color, colorStr):
    array1d = []
    for imgList in picArray:
        array1d += imgList
    for pic in array1d:
        colored_pixels = 0
        for pixel in pic.getdata():
            if pixel == color:
                colored_pixels += 1
        print(' ma: ' + str(colored_pixels) + " pixeli " + colorStr)

def testCreateFields():
    pustePole = Empty(1,2)
    print(pustePole)

def ClassifyScreen():
    picsDictionary, tempDict = loadDictionaries()
    tempDict = findThresholds2(tempDict, picsDictionary)
    #fieldsArray = createFields(tempDict)
    #return fieldsArray


def runTests():
    picsDictionary, tempDict = loadDictionaries()
    # testCreateFields()

    testColor(picsDictionary,(238,54,36), 'red')  #(0,0,0) czarny kolor

    #testColor(picsDictionary,(255,255,255), 'white')   #(255,255,255) bialy kolor
    # tempDict = findThresholds2(tempDict, picsDictionary)
    # testCompareAll(tempDict, picsDictionary)
    print("Test2")


    #1 heurystyka - zmierzenie czarnego koloru - obrazki powyzej 1600 zaklasyfikuj jako undiscovered
    #2 reszte obrazkow walnij do match template

#runTests()