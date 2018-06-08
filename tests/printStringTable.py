from PIL import Image, ImageDraw

def wydrukujTabliceStringow(tablicaStringow):

    img = Image.new('RGB', (1800, 1000))
    d = ImageDraw.Draw(img)

    offset_Y = 0
    for row in tablicaStringow:
        offset_X = 0
        for strin in row:
            d.text((offset_X, offset_Y), strin, fill=(255, 0, 0))
            offset_X += 50
        offset_Y += 50

    img.show()

if __name__ == "__main__":
    tablicaStringow = [["Und","Und","Und"],
                       ["Und", "Hero", "Undi"],
                       ["Und", "Und", "Und"]]
    wydrukujTabliceStringow(tablicaStringow)