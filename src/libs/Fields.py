
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


