import time
import pyautogui
import copy

from PIL import Image
import cv2
import numpy as np
from Comparing import *
from Fields import *
from Utility import *
from Tests2 import *
from Output import *


def classify_images(image_array):
    labeled_imaged_array = []
    testWithBlack(image_array,labeled_imaged_array)
    testWithWhite(image_array,labeled_imaged_array)
    testWithRed(image_array,labeled_imaged_array)
    print("asd")
    #spradz czy obrazki sie usuna

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
labeled_imaged_array = classify_images(image_array)
#field_class_array = create_fields(labeled_imaged_array)
#field = pick_move(field_class_array)
# make_move(field)

#todo: repair libraries so pycharm recognizes them as libraries
#todo: reformat everything so it is easily readable
#todo:refactor comments and variables to english

#todo: when making move remember to move a mouse out of the way and give it a few miliseconds before making printscreen
#it may introduce errors to computer vision algorithm

