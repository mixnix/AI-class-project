from PIL import Image
import numpy as np
import cv2


class TempTest:
    def __init__(self, img,friendClasses,name,threshold=0):
        self.img = img
        self.friendClasses = friendClasses
        self.name = name
        self.threshold = threshold

    def __str__(self):
        return "TempTest class"

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
        #"blood": oOther("blood", []),
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
    gameBoadPics1 = sliceImage(gameBoard1)
    t = lambda x, y: gameBoadPics1[x][y]

    gameBoard2 = Image.open("../res/2.png")
    gameBoadPics2 = sliceImage(gameBoard2)
    u = lambda x, y: gameBoadPics2[x][y]

    gameBoard3 = Image.open("../res/full_print_screen.png")
    gameBoadPics3 = sliceImage(gameBoard3)
    v = lambda x, y: gameBoadPics3[x][y]

    gameBoard4 = Image.open("../res/summonmonster.png")
    gameBoadPics4 = sliceImage(gameBoard4)
    uu = lambda x, y: gameBoadPics4[x][y]

    gameBoard5 = Image.open("../res/lemmisee.png")
    gameBoadPics5 = sliceImage(gameBoard5)
    uv = lambda x, y: gameBoadPics5[x][y]

    gameBoard6 = Image.open("../res/destroywall.png")
    gameBoadPics6 = sliceImage(gameBoard6)
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

def sliceImage(img):
    images_array = []
    slicesX = 20
    slicesY = 20

    left = 259

    #constants that in future should be generated automatically by detecting edges and calculating
    slice_sizeX = 48
    slice_sizeY = 48
    plusMovementX = 2
    plusMovementY = 2

    countX = 1


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
            upper += slice_sizeY + plusMovementY

            temp_list.append(working_slice)

            countY += 1

        left += slice_sizeX  + plusMovementX
        countX += 1
        images_array.append(temp_list)
    return images_array

def comparePicturesRetThreshold(image, template):
    image = np.array(image)
    template = np.array(template)

    img1_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, template_gray, cv2.TM_CCOEFF_NORMED )
    return res[0][0]

def findThresholds2(tempDict, picsDictionary):
    #show best threshold for each template

    varThresholdDetectionPossible = True
    contThresholdDetectionPossible = True

    absoluteMinRightThreshold = 1
    absoluteMaxWrongThreshold = 0
    for keyTemp in tempDict:
        minRightThreshold = 0.6
        maxWrongThreshold = 0
        for picKey in picsDictionary:
            for pic in picsDictionary.get(picKey):
                tempObject = tempDict.get(keyTemp)
                tempPic = tempObject.img

                similarity = comparePicturesRetThreshold(pic, tempPic)
                if(picKey == keyTemp):
                    if(similarity < minRightThreshold):
                        minRightThreshold = similarity
                elif(not tempObject.friendClasses.__contains__(picKey)):
                    if(similarity > maxWrongThreshold):
                        maxWrongThreshold = similarity
        tempDict.get(keyTemp).threshold = minRightThreshold
        if(minRightThreshold < absoluteMinRightThreshold):
            absoluteMinRightThreshold = minRightThreshold
        if(maxWrongThreshold > absoluteMaxWrongThreshold):
            absoluteMaxWrongThreshold = maxWrongThreshold
        if(minRightThreshold < maxWrongThreshold):
            varThresholdDetectionPossible = False

    if(absoluteMinRightThreshold < absoluteMaxWrongThreshold):
        contThresholdDetectionPossible = False

    print("Constant threshold template matching possible?: " + str(contThresholdDetectionPossible))
    print("Variable threshold template matching possible?: " + str(varThresholdDetectionPossible))
    return  tempDict

def compareWithThreshold(image, template, thresholdArg):
    image = np.array(image)
    template = np.array(template)

    img1_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, template_gray, cv2.TM_CCOEFF_NORMED )
    threshold = thresholdArg
    #print(res)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        if(pt[0] == pt[1]):
            return True
    return False

def compareWithThreshold2(image, template, thresholdArg):
    image = np.array(image)
    template = np.array(template)

    img1_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img1_gray, template_gray, cv2.TM_CCOEFF_NORMED )
    threshold = thresholdArg
    #print(res)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        if(pt[0] == pt[0] and pt[1] == pt[1]):
            return True
    return False
