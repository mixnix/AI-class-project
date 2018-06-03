def countFields(fieldArray):

    undisc = 0
    altar = 0
    empty = 0

    gold = 0
    hero = 0
    hidden_monster = 0
    hppotion = 0
    shop = 0
    wall = 0
    Goblin = 0
    MeatMan = 0
    Warlock = 0
    Zombie = 0
    blood = 0
    Bonus = 0
    Spell = 0
    for a in fieldArray:
        name = type(a).__name__
        if(name == 'Undiscovered'):
            undisc += 1
        elif(name == 'altar'):
            altar += 1
        elif(name == 'gold'):
            gold += 1
        elif(name == 'hero'):
            hero += 1
        elif(name == 'hidden_monster'):
            hidden_monster += 1
        elif(name == 'hppotion'):
            hppotion += 1
        elif(name == 'shop'):
            shop += 1
        elif(name == 'wall'):
            wall += 1
        elif(name == 'Goblin'):
            Goblin += 1
        elif(name == 'MeatMan'):
            MeatMan += 1
        elif(name == 'Warlock'):
            Warlock += 1
        elif(name == 'Zombie'):
            Zombie += 1
        elif(name == 'blood'):
            blood += 1
        elif(name == 'Bonus'):
            Bonus += 1
        elif(name == 'Spell'):
            Spell += 1
        elif(name == 'empty'):
            empty += 1

    #spells
    #undiscovered
    #monsters
    #empty
    #bonus
    #gold
    #hppotion
    print('undisc' + str(undisc))
    print("gold " +str(gold))
    print("hero" + str(hero))
    print("hidden_monster" + str(hidden_monster))
    print('hppotion ' + str(hppotion))
    print('shop ' + str(shop))
    print('wall ' + str(wall))
    print('Goblin ' + str(Goblin))
    print('MeatMan ' + str(MeatMan))
    print('Warlock ' + str(Warlock))
    print('Zombie ' + str(Zombie))
    print('blood ' + str(blood))
    print('Bonus ' + str(Bonus))
    print('Spell ' + str(Spell))
    print('empty ' + str(empty))


def testCompareAll(tempDict, picsDictionary):

    for picKey in picsDictionary:
        for pic in picsDictionary.get(picKey):
            for keyTemp in tempDict:

                if(picKey == keyTemp):
                    match = True
                else:
                    match = False
                #pic.show()
                print(picKey + " == " + keyTemp + " ?")
                tempObject = tempDict.get(keyTemp)
                #tempPic.show()
                comparison = compareWithThreshold(pic, tempObject.img, tempObject.threshold)
                print(comparison)
                if(picKey == keyTemp):
                    assert comparison
                elif(not tempObject.friendClasses.__contains__(picKey)):
                    assert not comparison
                #assert comparison == match
                print()

def testColor(picsDictionary,color,colorStr):
    for picKey in picsDictionary:
        for pic in picsDictionary.get(picKey):
            black = 0
            for pixel in pic.getdata():
                if pixel == color:
                    black += 1
            print(picKey + ' ma: ' + str(black) + " pixeli " + colorStr)

def countColorPixels(picArray, color, colorStr):
    array1d = []
    for imgList in picArray:
        array1d += imgList
    for pic in array1d:
        colored_pixels = 0
        for pixel in pic.getdata():
            if pixel == color:
                colored_pixels += 1
        print(' ma: ' + str(colored_pixels) + " pixeli " + colorStr)
