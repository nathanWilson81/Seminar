from PIL import Image
from turtle import *
import numpy as np
from skimage import io, img_as_float
from scipy import spatial
from math import sqrt
np.set_printoptions(threshold=np.inf)


def draw_square():
    begin_fill()
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    end_fill()


def draw_square2():
    setx(100)
    sety(100)
    clear()
    ht()
    begin_fill()
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    end_fill()


def eu_distance(x, y):
    return abs(x - y)

setup()
ts = getscreen()
draw_square()
can = ts.getcanvas()
can.postscript(file="sample.eps")
img = Image.open("sample.eps")
arr = img_as_float(img)
print("First image: \n")
print(arr.shape)
print(arr.mean())
img.save("test.png", "png")
############################# Second Picture Drawing ########################################
reset()
setup()
ts = getscreen()
draw_square2()
can = ts.getcanvas()
can.postscript(file="sample1.eps")
img1 = Image.open("sample1.eps")
arr1 = img_as_float(img1)
print("\nSecond image:\n")
print(arr1.shape)
print(arr1.mean())
img1.save("test1.png", "png")

print("\n How close the two images are (smaller better): \n")
print(eu_distance(arr.mean(), arr1.mean()))

done()
