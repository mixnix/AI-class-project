import pyautogui
import time
from PIL import Image

def slice(img, slicesX, slicesY):

    left = 259

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
            bbox = (left, upper, right, lower)
            working_slice = img.crop(bbox)
            upper += slice_sizeY

            temp_list.append(working_slice)

            countY += 1

        left += slice_sizeX
        countX += 1
        list_to_be_returned.append(temp_list)
    return list_to_be_returned


if __name__ == '__main__':
    time.sleep(2)

    #Take screenshot
    pic = pyautogui.screenshot()
    #Show the screenshot
    #pic.show()

    list_of_images = slice(pic,20,20)

    list_of_images[10][10].show()