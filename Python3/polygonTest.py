import os
from PIL import Image
import numpy as np
from skimage import img_as_float
np.set_printoptions(threshold=np.inf)

tri = []
quad = []
imgList = []
btmpList = []
pic = 1


def open_quads():
    for x in range(1, 20):
        image = Image.open(
            "/home/nathan/Seminar/imageEvolution/Python3/Quadrangles/Test" + str(x) + ".png")
        img = image.convert('L')
        img.save("test"+str(x+15)+".png")
        arr = img_as_float(img)
        quad.append(arr)
        imgList.append(img)


def open_tris():
    for x in range(1, 16):
        image = Image.open(
            "/home/nathan/Seminar/imageEvolution/Python3/Triangles/Test" + str(x) + ".png")
        img = image.convert('L')
        img.save("test"+str(x)+".png")
        arr = img_as_float(img)
        tri.append(arr)
        imgList.append(img)


def to_bitmap():
    for x in range(0, len(imgList)):
        tmp = imgList[0].convert('1')
        btmp = tmp.tobitmap()
        btmpList.append(btmp)


def eu_distance(x, y):
    return abs(x - y)


def test_average(testList):
    for x in range(0, (len(testList))):
        best = 1
        dist = 0
        for y in range(0, (len(testList))):
            dist = eu_distance(np.mean(testList[x]), np.mean(testList[y]))
            print("X=" + str(x) + ", Y=" + str(y) + ", distance between=" + str(dist))
            if((dist < best) and (dist > 0)):
                best = dist
                pic = y
        print("Best distance for picture " + str(x+1) + " was " + str(best) + " at Y = " + str(pic+1))

open_tris()
open_quads()
to_bitmap()
testList = tri + quad
test_average(testList)

for x in range(0, (len(testList))):
    print("Image " + str(x) + ": " + str(np.mean(testList[x])))
