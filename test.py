import sys
import time
import datetime
import pyautogui as py
from PIL import Image
from PIL import ImageFilter
import pytesseract
import numpy as np
import cv2

img = Image.open("testimage.png")
print(img.getcolors())
