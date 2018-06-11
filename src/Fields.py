
class Field:
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

class DifferentField(Field):
    def __str__(self):
        return "different field "

class Spell(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "spell "

class Undiscovered(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "undiscovered "

class Bonus(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "bonus "

class Monster(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y
        self.level = -1

    def __str__(self):
        return "monster "

class MeatMan(Monster):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y
        self.level = -1

    def __str__(self):
        return "meatman "

class Warlock(Monster):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y
        self.level = -1

    def __str__(self):
        return "warlock "


class Zombie(Monster):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y
        self.level = -1

    def __str__(self):
        return "zombie "

class Goblin(Monster):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y
        self.level = -1

    def __str__(self):
        return "goblin "


class altar(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "altar "


class blood(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "blood "

class empty(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "empty "

class gold(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "gold "

class hero(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "hero "

class hidden_monster(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "hidden monster "

class hppotion(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "hppotion "


class shop(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "shop "

class wall(Field):
    def __init__(self, x, y, pic):
        self.pic = pic
        self.positionX = x
        self.positionY = y

    def __str__(self):
        return "wall "





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
