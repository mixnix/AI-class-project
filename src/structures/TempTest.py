
class TempTest:
    def __init__(self, img,friendClasses,name,threshold=0):
        self.img = img
        self.friendClasses = friendClasses
        self.name = name
        self.threshold = threshold

    def __str__(self):
        return "TempTest class"