import pyautogui
import time
from PIL import Image
import cv2
import numpy as np

def slice(img):
    slicesX = 20
    slicesY = 20

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

def comparePictures(image1, image2):
    img1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    if(len(loc) > 0):
        return True
    else:
        return False


if __name__ == '__main__':
    time.sleep(2)

    #Take screenshot
    pic = pyautogui.screenshot()
    #Show the screenshot
    #pic.show()

    list_of_images = slice(pic)

    #show first picture
    list_of_images[6][5].show()  #goblin 2

    #prepare second picture
    img_with_goblin2 = Image.open("../res/2.png")
    list_with_goblin2 = slice(img_with_goblin2)
    #show sesond picture
    list_with_goblin2[1][10].show()


    image1 = np.array(list_of_images[6][5])
    image2 = np.array(list_with_goblin2[1][10])

    print(comparePictures(image1,image2))