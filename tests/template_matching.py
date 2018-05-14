import cv2
import numpy as np
from PIL import Image

def displayImage(imageArray):
    img = Image.fromarray(imageArray)
    img.show()

def displayMany(*arg):
    for argument in arg:
        displayImage(argument)

def testMonsterLevelDetection(monsterPath):
    detection_threshold = 0.95

    monsterImgArray = []
    for i in range(1,11):
        img_rgb = cv2.imread(monsterPath + str(i) + '.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        monsterImgArray.append(img_gray)

    levelImgArray = []
    for i in range(1,11):
        template = cv2.imread(monsterPath + "nr" + str(i) + '.png', 0)
        levelImgArray.append(template)
        w, h = template.shape[::-1]  #todo: bad coding practice, it doesnt neeed to be assigned many times

    monsterLevel = 1
    templateLevel = 1
    for monsterImg in monsterImgArray:
        print("\nPotwor o levelu: " + str(monsterLevel))
        for templateLevelImg in  levelImgArray:
            print("Template o levelu: " + str(templateLevel))
            res = cv2.matchTemplate(monsterImg, templateLevelImg, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= detection_threshold)
            for pt in zip(*loc[::-1]):
                print("pasuja do siebie")
            templateLevel += 1
        monsterLevel += 1
        templateLevel = 1

def matchTemplate():
    img_rgb = cv2.imread('../res/initial_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('../res/splitted_img/slice_dd_X_1_Y_2.png',0)
    w, h = template.shape[::-1]

    #Displays images
    #displayMany(img_rgb, img_gray, template)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv2.imshow('Detected', img_rgb)
    cv2.imwrite('detecting_template.jpg', img_rgb)

if __name__ == '__main__':
    testMonsterLevelDetection("../res/readyTemplates/Monsters/Goblin/")