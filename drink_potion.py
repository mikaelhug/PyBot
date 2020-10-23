import time
import pyautogui as py


def findimage(image):
    global mx, my
    image = "images/" + client + image + ".png"
    try:
        mx, my = py.locateCenterOnScreen(image, confidence=0.95)
        print("Found: " + image)
        return True
    except:
        return False

# Your setup
client = 'medivia/'
delay = 0.02
to_drink = 60 # How many mana fluid to drink

# Dont edit
mx = 0
my = 0
i = 0
lastmx = 0
wx, hx = py.size()
py.FAILSAFE = False

while i < to_drink:
    if findimage('manafluid'):
        if lastmx != mx:
            py.click(mx, my, button='left')
            time.sleep(delay/30)
            py.click(mx, my, button='right')
            time.sleep(delay/30)
            py.moveTo(wx/2+35, hx/2-55, delay)
            time.sleep(delay/30)
            py.click(button='left')
            time.sleep(delay*3)
            lastmx = mx
            i += 1

    else:
        break