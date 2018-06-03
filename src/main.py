import time
import pyautogui

from gettingValues import *
from inputProcessing import *
from creatingOutput import *




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

    # cutting printscreen into smaller pictures, one small picture contains one possible in game action
    image_array = sliceImage(print_screen)

    # creates class that specifies what kind of field that is, position x and y of that field in game and picture of that field
    labeled_imaged_array = classify_images(image_array, tempDict)

    # method that picks which field is the best move in game
    field = pick_move(labeled_imaged_array)

    # clicks picked field
    make_move(field)

