import pyautogui
import time

time.sleep(2)
#Take screenshot
pic = pyautogui.screenshot()

#Save the image
pic.save('Screenshot.jpg')