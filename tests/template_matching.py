import cv2
import numpy as np
from PIL import Image

if __name__ == '__main__':
    img_rgb = cv2.imread('../res/initial_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('../res/splitted_img/slice_dd_X_1_Y_2.png',0)
    w, h = template.shape[::-1]

    #Displays images
    img = Image.fromarray(img_rgb, 'RGB')
    img.show()

    img2 = Image.fromarray(img_gray)
    img2.show()

    img3 = Image.fromarray(template)
    img3.show()