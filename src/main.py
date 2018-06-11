import time
import pyautogui
from PIL import Image, ImageDraw

from gettingValues import *
from inputProcessing import *
from creatingOutput import *


def createBorderedImg(imageTable):


    vertical = Image.open('../res/debugging/vertical.png')
    horizontal = Image.open('../res/debugging/horizontal.png')
    borderImgTable = []
    for row in imageTable:
        tempRow = []
        for pic in row:
            tempRow.append(pic)
            tempRow.append(vertical)
        borderImgTable.append(tempRow)
        borderImgTable.append([horizontal])

    new_im = Image.new('RGB', (1800, 1000))


    y_offset = 0
    for ij in range(len(borderImgTable)):
        x_offset = 0
        max_height = 0
        for ik in range(len(borderImgTable[ij])):
            img = borderImgTable[ij][ik]
            new_im.paste(img, (x_offset, y_offset))
            x_offset += img.size[0]
            if max_height < img.size[1]:
                max_height = img.size[1]
        y_offset += max_height

    return new_im

def obroc(imgArray):
    newArray = []
    for column in image_array:
        newArray.append([])
    x = 0
    for column in image_array:
        y = 0
        for img in column:

            newArray[y].append(img)
            y += 1
        x += 1

    return newArray

def wydrukujTabliceStringow(tablicaStringow):

    img = Image.new('RGB', (1800, 1000))
    d = ImageDraw.Draw(img)

    offset_Y = 0
    for row in tablicaStringow:
        offset_X = 0
        for strin in row:
            d.text((offset_X, offset_Y), strin, fill=(255, 0, 0))
            offset_X += 50
        offset_Y += 50

    img.show()

def toStringArray(labeled_imaged_array):
    stringArray = [[] for i in range(20)]
    for obiekt in labeled_imaged_array:
        name = type(obiekt).__name__
        stringArray[obiekt.positionY].append((obiekt.positionX,name))

    changedStringArray = []
    for row in stringArray:
        sorted_by_first = sorted(row, key=lambda x: x[0])
        changedStringArray.append(sorted_by_first)

    finalStringArray = []
    for row in changedStringArray:
        finalStringArray.append([i[1][:7] for i in row])

    return finalStringArray







time.sleep(1)

#getting thresholds values
# loading images of templates that we will use for template matching and example pictures that we will use
# to get thresholds
picsDictionary, tempDict = loadDictionaries()
# comparing templates with example pictures to check if its possible to differentiate pictures into many different classes
# using match template metcho
tempDict = findThresholds2(tempDict, picsDictionary)

while not isWon():
    # taking printscreen
    print_screen = pyautogui.screenshot()

    #pokaz printscreena
    #print_screen.show()

    # cutting printscreen into smaller pictures, one small picture contains one possible in game action
    image_array = sliceImage(print_screen)

    #show sliced images to check if they are sliced properly
    obroconaArray = obroc(image_array)
    borderImg = createBorderedImg(obroconaArray)
    #borderImg.show()

    # creates class that specifies what kind of field that is, position x and y of that field in game and picture of that field
    labeled_imaged_array = classify_images(image_array, tempDict)
    stringArray = toStringArray(labeled_imaged_array)
    wydrukujTabliceStringow(stringArray)


    # method that picks which field is the best move in game
    field = pick_move(labeled_imaged_array)

    # clicks picked field
    make_move(field)

    sleep(5)

