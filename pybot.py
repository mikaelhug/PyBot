# pip3 install pyautogui opencv-python
# Ubuntu: sudo apt install scrot python3-tk python3-dev python3-pip

import time
import pyautogui as py
from PIL import Image
from random import randrange
from os import listdir

# Vars
client = 'medivia/'
delay = 0.5
runeloop = 5
mx = 0
my = 0
# spell = "encurso magni" # HMM
# spell = "encurso magni ignis" # GFB
spell = "encuro vita" # UH


py.FAILSAFE = False

# Actuals Functions
def findimage(image):
    global mx, my
    image = "images/" + client + image + ".png"
    try:
        mx, my = py.locateCenterOnScreen(image, confidence=0.95)
        print("Found: " + image)
        return True
    except:
        return False

def makerune():
    if findimage('blankrune'):
        rune_x, rune_y = mx, my
        py.click(x=rune_x, y=rune_y)
        time.sleep(delay)
        if findimage('handR'):
            py.dragTo(mx, my, button='left')
            time.sleep(delay)
            py.write(spell, interval=0.01)
            time.sleep(delay)
            py.press('enter')
            time.sleep(delay)
            py.dragTo(rune_x, rune_y, button='left')
            time.sleep(delay)

        elif findimage('handL'):
            py.dragTo(mx, my, button='left')
            time.sleep(delay)
            py.write(spell, interval=0.01)
            time.sleep(delay)
            py.press('enter')
            time.sleep(delay)
            for _ in range(0,2): # pull back twice on backup hand
                py.dragTo(rune_x, rune_y, button='left')
                time.sleep(delay)

def checkmana():
    if findimage('health'):
        mana90 = py.screenshot(region=(mx+110, my+32, 35, 15))
        colors = mana90.getcolors()
        for color in colors:
            if (color[1] == (114, 96, 255, 255)) or (color[1] == (114, 96, 255)):
                return True
        print("No mana.")
        return False

def eatfood():
    # Eat all foods in the food directory
    food_path = "images/" + client + "foods" 
    foods = listdir(food_path)
    had_food = 0
    for food in foods:
        food_img = "foods/"+food[:-4]
        if findimage(food_img):
            had_food = 1
            py.click(x=mx, y=my, button='right', clicks=5, interval=0.5)
            time.sleep(delay)
            break

    if had_food == 0:
        print("need to find food")

print("Your script is running...\n")

# Main loop
while True:
    try:
        if checkmana():
            for _ in range(0,runeloop):
                makerune()
            eatfood()

        else:
            eatfood()

    except:
        print("error")

    time.sleep(20+randrange(240))