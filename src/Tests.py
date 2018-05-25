from PIL import Image
from Comparing import *
from Fields import *
from Utility import *
def testComparePictures():
    oOther = lambda name : Image.open("../res/readyTemplates/Other/" + str(name) + ".png")
    oMonster = lambda name : Image.open("../res/readyTemplates/Other/" + str(name) + ".png")
    tempDict = {
        "altar" : oOther("altar"),
        "blood" : oOther("blood"),
        #"bonusatk" : oOther("bonusatk"),
        "bonushp" : oOther("bonushp"),
        #"bonusmp" : oOther("bonusmp"),
        #"burndayraz" : oOther("burndayraz"),  #spell
        #"bysspes" : oOther("bysspes"), #spell
        "empty" : oOther("empty"),
        #"getindare" : oOther("getindare"), #spell
        "gold" : oOther("gold"),
        "hero" : oOther("hero"),
        "hidden_monster" : oOther("hidden_monster"),
        "hppotion" : oOther("hppotion"),
        #"imawal" : oOther("imawal"), #spell
        #"lemmisi" : oOther("lemmisi"), #spell
        #"mppotion" : oOther("mppotion"), #other potion
        #"pisorf" : oOther("pisorf"), #spell
        "shop" : oOther("shop"),
        #"tele" : oOther("tele"), #spell
        #"undiscovered" : oOther("undiscovered"),
        #"waldes" : oOther("waldes"), #spell
        "wall" : oOther("wall"),
        #"wonafyt" : oOther("wonafyt"), #spell

        #shopp
        #fireball, burndayraz
        #destroy wall, endiswal
        #teleportation
        #tele monster away, pisorf
        # first strike, getindare
        # +30 attack spekk, bysseps
        # hp potion - if it wont work then I will just detect whether theres potion there,
        # I wont differentiate
        # mana potion
        # attack bonus
        # hp bonus
        # mana bonus
        # empty with blood

        #summon monster, wonafyt
        #turns enemy into stone, imawal
        #destroy wall
        # show 3 random blocks, lemmisi




        #meatMan - from games files?,firstly try to match all levels, but remember
            # to test all levels from 1 to 10 when teseting wheter template matching is
            #possible
        #warlock - jw
        #goblin - jw
        #zombie


        #all possible spells around 6

        #field that lower level momnster was but got summoned by a spell
        #dont use lemme see

        #later - implement detection of ignited altar

        #possible tricks - check on right side of screen whether its monster, if its monster
        #then the screen will change, if its something different then it
        #wont, is walkable over
        #

    }

    # for key in tempDict:
    #     tempDict.get(key).show()

    gameBoard1 = Image.open("../res/initial_screen.png")
    gameBoadPics1 = slice(gameBoard1)
    t = lambda x,y : gameBoadPics1[x][y]

    gameBoard2 = Image.open("../res/2.png")
    gameBoadPics2 = slice(gameBoard2)
    u = lambda x,y : gameBoadPics2[x][y]

    gameBoard3 = Image.open("../res/full_print_screen.png")
    gameBoadPics3 = slice(gameBoard3)
    v = lambda x,y : gameBoadPics3[x][y]

    gameBoard4 = Image.open("../res/summonmonster.png")
    gameBoadPics4 = slice(gameBoard4)
    uu = lambda x,y : gameBoadPics4[x][y]

    gameBoard5 = Image.open("../res/lemmisee.png")
    gameBoadPics5 = slice(gameBoard5)
    uv = lambda x, y: gameBoadPics5[x][y]

    gameBoard6 = Image.open("../res/destroywall.png")
    gameBoadPics6 = slice(gameBoard6)
    ut = lambda x, y: gameBoadPics6[x][y]

#11, 14
    picsDictionary = {
        "altar" : [t(12,0),v(8,0)],
        "blood": [u(6,15),u(11,16),u(14,15)],
        #"bonusatk": [u(8,5),u(14,6)],
        "bonushp": [u(2,4),v(6,2)],
        #"bonusmp": [u(5,4),v(11,8)],
        #"burndayraz": [u(8,9),v(10,17)], #spell
        #"bysspes": [u(16,19), uu(8,10)], #spell
        "empty" : [t(2,0),t(2,2)],
        #"getindare": [u(16,10),v(16,14)], #spell
        "gold" : [t(4,17),t(6,18)],
        "hero" : [t(6,2),u(7,12)],
        "hidden_monster" : [t(16,8),t(16,14)],
        "hppotion": [u(14,1),u(14,8)],
        #"imawal": [u(10,3),v(10,16)], #spell
        #"lemmisi": [uv(9,9)], #spell
        #"mppotion": [u(16,9),u(17,11)], #other potion
        #"pisorf": [v(7,8)], #spell
        "shop" : [t(2,1),t(8,6)],
        #"tele": [v(6,5), uu(8,11)], #spell
        "undiscovered" : [t(0,0),t(8,0),t(0,5),t(13,15)],
        #"waldes": [ut(11,14)], #spell
        "wall" : [t(1,0),t(0,1),t(1,1)],
        #"wonafyt": [v(7,8), uu(8,8)], #spell
    }

    # , lemmisi, ,  , waldes, wonafyt

    #picsDictionary.get()


    # for key in picsDictionary:
    #     for l in range(len(picsDictionary.get(key))):
    #         picsDictionary.get(key)[l].show()


    findThresholds(tempDict, picsDictionary)
    # testCompareAll(tempDict, picsDictionary)

def findThresholds(tempDict, picsDictionary):
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
                tempPic = tempDict.get(keyTemp)

                similarity = comparePicturesRetThreshold(pic, tempPic)
                if(picKey == keyTemp):
                    if(similarity < minRightThreshold):
                        minRightThreshold = similarity
                else:
                    if(similarity > maxWrongThreshold):
                        maxWrongThreshold = similarity
        if(minRightThreshold < absoluteMinRightThreshold):
            absoluteMinRightThreshold = minRightThreshold
        if(maxWrongThreshold > absoluteMaxWrongThreshold):
            absoluteMaxWrongThreshold = maxWrongThreshold
        print("Key: " + keyTemp)
        print("minimum right threshold = " + str(minRightThreshold))
        print("maximum wrong threshold = " + str(maxWrongThreshold))
        print()
        if(minRightThreshold < maxWrongThreshold):
            varThresholdDetectionPossible = False

    if(absoluteMinRightThreshold < absoluteMaxWrongThreshold):
        contThresholdDetectionPossible = False

    print("Constant threshold template matching possible?: " + str(contThresholdDetectionPossible))
    print("Variable threshold template matching possible?: " + str(varThresholdDetectionPossible))

def testCompareAll(tempDict, picsDictionary):

    for picKey in picsDictionary:
        for pic in picsDictionary.get(picKey):
            for keyTemp in tempDict:
                if(picKey == keyTemp):
                    match = True
                else:
                    match = False
                #pic.show()
                print(picKey)
                tempPic = tempDict.get(keyTemp)
                #tempPic.show()
                comparison = comparePictures(pic, tempPic)
                print(comparison)
                #assert comparison == match
                print()


def testCreateFields():
    pustePole = Empty(1,2)
    print(pustePole)

def runTests():
    # testCreateFields()
    testComparePictures()