import copy
from PIL import Image
from Fields import *
from gettingValues import compareWithThreshold
from PIL import ImageGrab
import pyautogui
import time




def classify_images(image_array, tempDict):
    labeled_imaged_array = []
    testWithBlack(image_array,labeled_imaged_array)
    testWithWhite(image_array,labeled_imaged_array)
    testWithRed(image_array,labeled_imaged_array)
    testWithBloodyRed(image_array,labeled_imaged_array)
    templateClassifying(image_array,labeled_imaged_array, tempDict)

    initiatingMonsterLevels(labeled_imaged_array)

    return labeled_imaged_array


def initiatingMonsterLevels(labeled_imaged_array):
    bbox = (0, 24, 24, 48)

    monsterImages = []
    loadMonster = lambda lvl, monsterName : Image.open("../res/readyTemplates/Monsters/" + monsterName + "/" + str(lvl) + ".png")


    for lvl in range(1,11):
        monsterImages.append(loadMonster(lvl, "Goblin"))
        monsterImages.append(loadMonster(lvl, "MeatMan"))
        monsterImages.append(loadMonster(lvl, "Warlock"))
        monsterImages.append(loadMonster(lvl, "Zombie"))

    monsterLvlImage = []
    for img in monsterImages:
        working_slice = img.crop(bbox)
        monsterLvlImage.append(working_slice)

    for field in labeled_imaged_array:
        if type(field).__name__ in ["MeatMan", "Goblin", "Warlock", "Zombie"]:
            if (testGreenLevels(field.pic) > 20):
                classifyLevel(field, 'green')
                print("zielona kategoria")
            elif (testYellowLevels(field.pic) > 20):
                classifyLevel(field, 'green')
                print("zolta kategoria")
            elif (testOrangeLevels(field.pic) > 5):
                print("orange category")
            else:
                print("red category")




    #type(field).__name__ == "Warlock":
    print("test stop")

def classifyLevel(field, category):
    #enlarge picture
    moveMouse(field)
    print("test classifying level, move mouse")

def moveMouse(field):
    x = 259 + (field.positionX + 1) * 48
    y = 10 + (field.positionY + 1) * 48

    pyautogui.moveTo(x, y)



def testGreenLevels(img):
    return countColorPixels(img,(0,100,0),(0,255,0))

def testYellowLevels(img):
    count = 0
    for pixel in img.getdata():
        if pixel[2] == 0 and pixel[0] == pixel[1] and pixel[0] > 30:
            count += 1

    return count


def testOrangeLevels(img):
    count = 0
    for pixel in img.getdata():
        if pixel[2] == 0 and pixel[0] == 2*pixel[1] and pixel[0] > 130:
            count += 1

    return count

def testRedLevels(img):
    return countColorPixels(img,(100,0,0),(255,0,0))




def countColorPixels(img, color):
    count = 0
    for pixel in img.getdata():
        if pixel == color:
            count += 1
    return count

def countColorPixels(img, colorMin, colorMax):
    count = 0
    for pixel in img.getdata():
        if pixel > colorMin and pixel < colorMax:
            count += 1
    return count


def templateClassifying(image_array,labeled_array, templateDictionary):
    image_array_copy = copy.deepcopy(image_array)
    filling_image = Image.open("../res/green.png")
    x = 0
    for pic_row in image_array_copy:
        y = 0
        for pic in pic_row:
            for templateKey in templateDictionary:
                templateObject = templateDictionary.get(templateKey)
                if(compareWithThreshold(pic,templateObject.img, templateObject.threshold)):
                    newObjectString = "labeled_array.append("+str(templateKey)+"(x,y,pic))"
                    exec(newObjectString)
                    #debuging
                    image_array[x][y] = filling_image
            y += 1
        x+= 1

        #template comparison with threshold
        #if true then create a class and input into array


def testWithBlack(image_array,labeled_array):
    labeled_imaged_array = []
    image_array_copy = copy.deepcopy(image_array)
    filling_image = Image.open("../res/green.png")
    x = 0
    for pic_row in image_array_copy:
        y = 0
        labeled_row = []
        for pic in pic_row:
            black = 0
            for pixel in pic.getdata():
                if pixel == (0,0,0):
                    black += 1
        #tu testuj czy jest zakleciem
            if black > 1400:
                labeled_array.append(Undiscovered(x,y,pic))
                image_array[x][y] = filling_image #34,177,76

            elif black > 200:
                labeled_array.append(Spell(x,y,pic))
                image_array[x][y] = filling_image

            y += 1

        x += 1

    return labeled_imaged_array

def testWithWhite(image_array,labeled_array):
    labeled_imaged_array = []
    image_array_copy = copy.deepcopy(image_array)
    filling_image = Image.open("../res/green.png")

    x = 0
    for pic_row in image_array_copy:
        y = 0
        labeled_row = []
        for pic in pic_row:
            white = 0
            for pixel in pic.getdata():
                if pixel == (255,255,255):
                    white += 1
        #tu testuj czy jest zakleciem
            if white > 100:
                labeled_array.append(Bonus(x,y,pic))
                image_array[x][y] = filling_image

            y += 1

        x += 1

    return labeled_imaged_array


def testWithRed(image_array,labeled_array):
    labeled_imaged_array = []
    image_array_copy = copy.deepcopy(image_array)
    filling_image = Image.open("../res/green.png")

    x = 0
    for pic_row in image_array_copy:
        y = 0
        labeled_row = []
        for pic in pic_row:
            red = 0
            for pixel in pic.getdata():
                if pixel == (238,54,36):
                    red += 1
        #tu testuj czy jest zakleciem
            if red > 80:
                labeled_array.append(MeatMan(x,y,pic))
                image_array[x][y] = filling_image

            y += 1

        x += 1

    return labeled_imaged_array

def testWithBloodyRed(image_array,labeled_array):
    labeled_imaged_array = []
    image_array_copy = copy.deepcopy(image_array)
    filling_image = Image.open("../res/green.png")

    x = 0
    for pic_row in image_array_copy:
        y = 0
        labeled_row = []
        for pic in pic_row:
            red = 0
            for pixel in pic.getdata():
                if pixel == (237,18,18):
                    red += 1
        #tu testuj czy jest zakleciem
            if red > 150:
                labeled_array.append(blood(x,y,pic))
                image_array[x][y] = filling_image

            y += 1

        x += 1

    return labeled_imaged_array


