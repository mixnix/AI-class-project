import sys
from PIL import Image

def test(imageTable):


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
    for row in borderImgTable:
        x_offset = 0
        max_height = 0
        for img in row:
            new_im.paste(img, (x_offset, y_offset))
            x_offset += img.size[0]
            if max_height < img.size[1]:
                max_height = img.size[1]
        y_offset += max_height

    new_im.show()
    new_im.save('test.jpg')

if __name__ == "__main__":
    im1 = Image.open('Test1.jpg')
    im2 = Image.open('Test1.jpg')
    im3 = Image.open('Test1.jpg')
    im4 = Image.open('Test1.jpg')
    im5 = Image.open('Test1.jpg')
    im6 = Image.open('Test1.jpg')
    im7 = Image.open('Test1.jpg')
    im8 = Image.open('Test1.jpg')
    im9 = Image.open('Test1.jpg')
    imageTable = [[im1,im2,im3],
                  [im4,im5,im6],
                  [im7,im8,im9]]
    borderImgTable = test(imageTable)
    borderImgTable.show()