
from PIL import Image
import math
import os

# slices image in height and width, it will have slicesX slices in width and slicesY slices in height
def slice(image_path, out_name, outdir, slicesX, slicesY):
    img = Image.open(image_path)

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
        for Y in range(slicesY):
            lower = upper + slice_sizeY

            equalizer = 0
            bbox = (left+equalizer, upper+equalizer, right+equalizer, lower+equalizer)
            working_slice = img.crop(bbox)
            upper += slice_sizeY + plusMovementY
            working_slice.save(os.path.join(outdir, "../res/splitted_img/slice_" +
                                            out_name + "_X_" + str(countX) + "_Y_" + str(countY) + ".png"))

            countY += 1

        left += slice_sizeX + plusMovementX
        countX += 1

if __name__ == '__main__':
    #long_slice("../res/initial_screen.png","dd", os.getcwd(), 300)
    slice("../res/destroywall.png","dd", os.getcwd(), 20, 20)