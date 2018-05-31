import pyautogui as ag

#
def clickField(x, y):
    initialX = 275;
    initialY = 45;
    ag.click(initialX+x*50,initialY+y*50)