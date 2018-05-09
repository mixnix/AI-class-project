
from PIL import Image
import math
import os

def long_slice(image_path, out_name, outdir, slice_size):
    """slice an image into parts slice_size tall"""
    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))

    count = 1
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)

        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        working_slice.save(os.path.join(outdir, "../res/vertically_splitted_img/slice_" + out_name + "_" + str(count)+".png"))
        count +=1

# slices image in height and width, it will have slicesX slices in width and slicesY slices in height
def slice(image_path, out_name, outdir, slicesX, slicesY):
    img = Image.open(image_path)
    left = 259

    #constants that in future should be generated automatically by detecting edges and calculating
    slice_sizeX = 50
    slice_sizeY = 50

    countX = 1
    for X in range(slicesX):
        right = left + slice_sizeX


        upper = 30
        countY = 1
        for Y in range(slicesY):
            lower = upper + slice_sizeY

            bbox = (left, upper, right, lower)
            working_slice = img.crop(bbox)
            upper += slice_sizeY
            working_slice.save(os.path.join(outdir, "../res/splitted_img/slice_" +
                                            out_name + "_X_" + str(countX) + "_Y_" + str(countY) + ".png"))
            upper += slice_sizeY
            countY += 1

        left += slice_sizeX
        countX += 1

if __name__ == '__main__':
    long_slice("../res/initial_screen.png","dd", os.getcwd(), 300)
    slice("../res/initial_screen.png","dd", os.getcwd(), 20, 20)