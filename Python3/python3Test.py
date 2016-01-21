from PIL import Image
from turtle import *
import numpy as np
from skimage import io, img_as_float
from scipy import spatial
from math import sqrt
import random
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


def draw_image(x):
    ts = getscreen()
    #height = random.randrange(0, 128)
    #width = random.randrange(0, 128)
    # setx(height)
    # sety(width)
    clear()
    ht()
    # begin_fill()
    forward(random.randrange(0, 128))
    right(random.randrange(0, 360))
    forward(random.randrange(0, 128))
    right(random.randrange(0, 360))
    forward(random.randrange(0, 128))
    right(random.randrange(0, 360))
    forward(random.randrange(0, 128))
    right(random.randrange(0, 360))
    home()
    # end_fill()
    can = ts.getcanvas()
    can.postscript(file="testing" + str(x) + ".eps")
    img = Image.open("testing" + str(x) + ".eps")
    img.save("testing" + str(x) + ".png", "png")


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
############################# Second Picture Drawing #####################
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

for x in range(0, 100):
    draw_image(x)

done()
