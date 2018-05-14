from PIL import Image

def cut_out_numbers(image_path):
    for x in range(1,11):
        img = Image.open(image_path + str(x) + ".jpg")
        left = 0
        upper = 33
        right = 12
        lower = 50
        bbox = (left, upper, right, lower)
        number_img = img.crop(bbox)
        number_img.save(image_path + "nr" + str(x) + ".png")

if __name__ == "__main__":
    cut_out_numbers("../res/readyTemplates/Monsters/Goblin/")
