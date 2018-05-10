import pyautogui
import time

if __name__ == '__main__':
    time.sleep(2)

    #Take screenshot
    pic = pyautogui.screenshot()
    #Show the screenshot
    pic.show()