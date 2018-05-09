import pyautogui
import time

if __name__ == '__main__':
    time.sleep(2)
    #Take screenshot
    pic = pyautogui.screenshot()
    #Save the image
    pic.save('Screenshot.jpg')