import time
import pyautogui
from random import randint
import copy

from PIL import Image
import cv2
import numpy as np
from Comparing import  *
from Fields import *
from Utility import *
from Tests2 import *
from Output import *


def classify_images(image_array, tempDict):
    labeled_imaged_array = []
    testWithBlack(image_array,labeled_imaged_array)
    testWithWhite(image_array,labeled_imaged_array)
    testWithRed(image_array,labeled_imaged_array)
    testWithBloodyRed(image_array,labeled_imaged_array) #237,18,18
    templateClassifying(image_array,labeled_imaged_array, tempDict)

    # for a in range(30,len(labeled_imaged_array)):
    #     labeled_imaged_array[a].pic.show()

    return labeled_imaged_array
    print("asd")
    #spradz czy obrazki sie usuna

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





def slicePrintScreen(img):
    images_array =[]
    slicesX = 20
    slicesY = 20

    left = 259 + 2

    #constants that in future should be generated automatically by detecting edges and calculating
    slice_sizeX = 48
    slice_sizeY = 48
    plusMovementX = 2
    plusMovementY = 2

    countX = 1
    for X in range(slicesX):
        right = left + slice_sizeX


        upper = 30 + 2
        countY = 1
        temp_image_array = []
        for Y in range(slicesY):
            lower = upper + slice_sizeY

            equalizer = 0
            bbox = (left+equalizer, upper+equalizer, right+equalizer, lower+equalizer)
            working_slice = img.crop(bbox)
            upper += slice_sizeY + plusMovementY
            temp_image_array.append(working_slice)

            countY += 1
        images_array.append(temp_image_array)
        left += slice_sizeX + plusMovementX
        countX += 1
    return images_array

def countFields(fieldArray):

    undisc = 0
    altar = 0
    empty = 0

    gold = 0
    hero = 0
    hidden_monster = 0
    hppotion = 0
    shop = 0
    wall = 0
    Goblin = 0
    MeatMan = 0
    Warlock = 0
    Zombie = 0
    blood = 0
    Bonus = 0
    Spell = 0
    for a in fieldArray:
        name = type(a).__name__
        if(name == 'Undiscovered'):
            undisc += 1
        elif(name == 'altar'):
            altar += 1
        elif(name == 'gold'):
            gold += 1
        elif(name == 'hero'):
            hero += 1
        elif(name == 'hidden_monster'):
            hidden_monster += 1
        elif(name == 'hppotion'):
            hppotion += 1
        elif(name == 'shop'):
            shop += 1
        elif(name == 'wall'):
            wall += 1
        elif(name == 'Goblin'):
            Goblin += 1
        elif(name == 'MeatMan'):
            MeatMan += 1
        elif(name == 'Warlock'):
            Warlock += 1
        elif(name == 'Zombie'):
            Zombie += 1
        elif(name == 'blood'):
            blood += 1
        elif(name == 'Bonus'):
            Bonus += 1
        elif(name == 'Spell'):
            Spell += 1
        elif(name == 'empty'):
            empty += 1

    #spells
    #undiscovered
    #monsters
    #empty
    #bonus
    #gold
    #hppotion
    print('undisc' + str(undisc))
    print("gold " +str(gold))
    print("hero" + str(hero))
    print("hidden_monster" + str(hidden_monster))
    print('hppotion ' + str(hppotion))
    print('shop ' + str(shop))
    print('wall ' + str(wall))
    print('Goblin ' + str(Goblin))
    print('MeatMan ' + str(MeatMan))
    print('Warlock ' + str(Warlock))
    print('Zombie ' + str(Zombie))
    print('blood ' + str(blood))
    print('Bonus ' + str(Bonus))
    print('Spell ' + str(Spell))
    print('empty ' + str(empty))



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



time.sleep(1)

#thresholds = get_thresholds()
picsDictionary, tempDict = loadDictionaries()
tempDict = findThresholds2(tempDict, picsDictionary)

#petla ktora caly czas dziala

#print_screen = do_printscreen()
print_screen = pyautogui.screenshot()

#image_array = slice_printscreen(print_screen)
image_array = slicePrintScreen(print_screen) #doesnt cut out images properly, may have to move it
# a little to the left (all of them)



#labeled_imaged_array = classify_images(image_array)
    #returns  array of tuples, label is string describing what is on picture and image is image sliced from printscreen
    #detect spells by color - black?
    #detect bonuses by color - white?
    #detect meat man by red
    #template mathing
labeled_imaged_array = classify_images(image_array, tempDict)
field = pick_move(labeled_imaged_array)
make_move(field)

#countFields(labeled_imaged_array)


#todo: repair libraries so pycharm recognizes them as libraries
#todo: reformat everything so it is easily readable
#todo:refactor comments and variables to english

#todo: when making move remember to move a mouse out of the way and give it a few miliseconds before making printscreen
#todo: create rules for naming functions, local variables and classes and reformat everything so it follows these rules
#it may introduce errors to computer vision algorithm

