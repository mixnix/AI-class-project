
class Field:
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y

class DifferentField(Field):
    def __str__(self):
        return "d "

class Undiscovered(Field):
    def __str__(self):
        return "u "

class Altar(Field):
    def __str__(self):
        return "a "

class Empty(Field):
    def __str__(self):
        return "e "

class Gold(Field):
    def __str__(self):
        return "g "

class Hero(Field):
    def __str__(self):
        return "h "

class HiddenMonster(Field):
    def __str__(self):
        return "hm "

class Shop(Field):
    def __str__(self):
        return "a "

class Wall(Field):
    def __str__(self):
        return "w "

class Monster(Field):
    def __str__(self):
        return "m "


def createTile(name,x,y):
    tileProducer = {
        #todo: are those tiles, gonna be the same object??? with the same adress
        "undiscovered" : Undiscovered(x,y),
        "altar" : Altar(x,y),
        "empty": Empty(x, y),
        "gold": Gold(x, y),
        "hero": Hero(x, y),
        "hidden_monster": HiddenMonster(x, y),
        "shop": Shop(x, y),
        "wall": Wall(x, y),

    }
    return tileProducer.get(name, DifferentField(x,y))