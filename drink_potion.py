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
delay = 0.1
to_drink = 40 # How many mana fluid to drink

# Dont edit
mx = 0
my = 0
wx, hx = py.size()
py.FAILSAFE = False

for _ in range(0, to_drink):
    if findimage('manafluid'):
        py.click(mx, my, button='left')
        time.sleep(delay/10)
        py.click(mx, my, button='right')
        time.sleep(delay/10)
        py.moveTo(wx/2+35, hx/2-55, delay)
        time.sleep(delay/10)
        py.click(button='left')
        time.sleep(delay)

    else:
        break