import copy
from PIL import Image
from Fields import *
from gettingValues import compareWithThreshold

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

