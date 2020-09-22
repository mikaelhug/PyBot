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
runeloop = 3
mx = 0
my = 0
wx, hx = py.size()
#spell = "encurso magni" # HMM
spell = "encurso magni ignis" # GFB
#spell = "encuro vita" # UH


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

def freehand():
    print("Removing object from right hand")

    if findimage('helmet'):
    	sx = mx+35
    	sy = my+55
    	
    	py.click(sx, sy)
    	time.sleep(1)
    	py.dragTo(wx/2-100, hx/2, delay*3, button='left')
    	time.sleep(delay)

def makerune(handx, handy):
    if findimage('blankrune'):
        rune_x, rune_y = mx, my
        py.click(x=rune_x, y=rune_y)
        time.sleep(delay)
        py.dragTo(handx, handy, delay, button='left')
        time.sleep(delay)
        py.write(spell, interval=0.01)
        time.sleep(delay)
        py.press('enter')
        time.sleep(delay+0.5)
        py.dragTo(rune_x, rune_y, delay, button='left')
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

def killdwarf():
    print("Killing Dwarfs")
    mark=1
    while True:
        time.sleep(delay)
        if findimage('dwarf_attack'):
            time.sleep(2)
            eatfood()
        elif findimage('dwarf_attack2'):
            time.sleep(2)
        elif findimage('dwarf2'):
            py.click(x=mx+30, y=(my+5))
            time.sleep(delay)
        elif findimage('dwarf'):
            py.click(x=mx+30, y=(my+5))
            time.sleep(delay)
            py.write("incuro", interval=0.01)
            time.sleep(delay)
            py.press('enter')
        else:
            print("No dwarfs, walking")
            if mark == 6:
                mark = 1
            mark_str = "marks/" + str(mark)
            if findimage(mark_str):
                py.click(x=mx, y=my)
                time.sleep(10) # Allow for walking. Smarter way?
                mark += 1

def fish():
    print("Fishing ...\n")
    base_x = 680; base_y = 785
    length_x = 1090; length_y = 400
    
    #water = py.screenshot(region=(base_x, base_y, length_x, length_y))
    #water.save('/home/botter/PyBot/water.png')
    for _ in range(0,50):
        if findimage("fishingrod"):
            py.click(mx, my)
            time.sleep(0.05)
            py.click(mx, my, button='right')
            time.sleep(0.1)
            py.click(base_x+randrange(length_x), base_y+randrange(length_y))
            time.sleep(2)
    else:
        print("No fishingrod")
        time.sleep(10)

# Main loop
print("Your script is running...\n")
while True:
    try:
        if checkmana():
            if not findimage('handR'):
                freehand()

            findimage('handR')
            handx, handy = mx, my
            for _ in range(0,runeloop):
                makerune(handx, handy)
            eatfood()

        else:
            time.sleep(20+randrange(240)) # OR FISH
            #fish()
            eatfood()

    except:
        print("error")