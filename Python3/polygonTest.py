import os
from PIL import Image
import numpy as np
from skimage import img_as_float
import ssim
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

tri = []
quad = []
imgList = []
btmpList = []
pic = 1
mseArray = np.zeros((35, 35))
ssimArray = np.zeros((35, 35))
avgArray = np.zeros((35, 35))


def open_quads():
    for x in range(1, 20):
        image = Image.open(
            "/home/nathan/Seminar/imageEvolution/Python3/Quadrangles/Test" + str(x) + ".png")
        img = image.convert('L')
        img.save("test" + str(x + 15) + ".png")
        arr = img_as_float(img)
        quad.append(arr)
        imgList.append(img)


def open_tris():
    for x in range(1, 16):
        image = Image.open(
            "/home/nathan/Seminar/imageEvolution/Python3/Triangles/Test" + str(x) + ".png")
        img = image.convert('L')
        img.save("test" + str(x) + ".png")
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
            avgArray[x][y] = dist
            # print("X=" + str(x) + ", Y=" + str(y) + ", distance between=" +
            # str(dist))
            if((dist < best) and (dist > 0)):
                best = dist
                pic = y
        # print("Best distance for Test Image " + str(x + 1) +
        #      " was " + str(best) + " at Test Image " + str(pic + 1))


def test_ssim():
    for x in range(0, (len(imgList))):
        best = 0
        sim = 0
        for y in range(0, (len(imgList))):
            sim = ssim.compute_ssim(imgList[x], imgList[y])
            ssimArray[x][y] = sim
            if((sim > best)and(sim < 1)):
                best = sim
                pic = y
        # print("Best SSIM for Test Image " + str(x + 1) + " was " +
        #      str(best) + " at Test Image " + str(pic + 1))


def test_mse(testList):
    for x in range(0, (len(testList))):
        best = 1
        mse = 0
        for y in range(0, (len(testList))):
            err = np.sum((testList[x] - testList[y])**2)
            err /= float(363 * 363)
            mseArray[x][y] = err
            if((err < best)and(err > 0)):
                best = err
                pic = y
        # print("Best MSE for Test Image " + str(x + 1) + " was " +
        #      str(best) + " at Test Image " + str(pic + 1))


def normalizeArray(arr):
    for x in range(0, (len(testList))):
        arr[x] = arr[x] / arr[x].max()
        #arr[x] = arr[x] / arr[x].max()
    return arr


def normalizeSSIM(arr):
    for x in range(0, (len(imgList))):
        arr[x] = (arr[x] - arr[x].min()) / (arr[x].max() - arr[x].min())
    return arr


open_tris()
open_quads()
to_bitmap()
testList = tri + quad
img = Image.open("/home/nathan/Seminar/imageEvolution/Python3/test35.png")
con = img.convert('L')
imgList.append(con)
arr = img_as_float(con)
testList.append(arr)
#print("Testing for Mean Squared Error \n")
test_mse(testList)
#print("Testing for Average Distance \n")
test_average(testList)
#print("Testing for SSIM\n")
#test_ssim()
normAvg = normalizeArray(avgArray)
normMse = normalizeArray(mseArray)
#normSsim = normalizeSSIM(ssimArray)
print("Normalized SSIM\n")
print(normAvg[0])
#best = normAvg[0].argsort()[:4]
# print("The three best images for Image 1 in order are: " +
#      str(best[1] + 1) + ", " + str(best[2] + 1) + ", " + str(best[3] + 1))
#for x in range(0, (len(testList))):
    #best = normAvg[x].argsort()[-4:][::-1]
#    best = normAvg[x].argsort()[:4]
#    print("The three worst images for Image " + str(x + 1) + " in order are: " +
#          str(best[0] + 1) + ", " + str(best[1] + 1) + ", " + str(best[2] + 1))
#    top = int(normAvg[x][best[0]] * 100)
#    middle = int(normAvg[x][best[1]] * 100)
#    last = int(normAvg[x][best[2]] * 100)
#    print(str(top)+"%, "+str(middle)+"%, "+str(last)+"%")

#print("Normalized MSE\n")
# print(normMse)
#print("Normalized SSIM\n")
# print(normSsim)
