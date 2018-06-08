import sys
from PIL import Image

im1 = Image.open('Test1.jpg')
im2 = Image.open('Test2.jpg')
im3 = Image.open('Test3.jpg')
images = [im1,im2,im3]

a =  (i.size for i in images)
widths, heights = zip(*(a))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
images = [im1,im2,im3]
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.show()
new_im.save('test.jpg')