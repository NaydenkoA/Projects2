import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import os
import math

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_train = x_train.reshape((x_train.shape[0], 28, 28))
img = Image.fromarray(x_train[0])
img.show()

def getAvarage(arr):
    if len(arr) == 0:
        return 0
    n = 0
    s = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            n = n + 1
            s = s + arr[i][j]
    return s/n

def reShape(img,a,b):
    if a == b:
        return img.resize((a, a))
    if a > b:
        img = img.resize((a, a))
        return img
    else:
        img = img.resize((b, b))
        return img


def findCenter(arr):
    m = 0
    i_center = 0
    j_center = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            m = m + arr[i][j]/255
            i_center = i_center + arr[i][j]/255*i
            j_center = j_center + arr[i][j]/255*j
    if m == 0:
        return [math.floor(len(arr)/2), math.floor(len(arr[0])/2)]
    else:
        return [math.floor(i_center/m), math.floor(j_center/m)]


def centrizePic(img):
    arr = np.asarray(img)
    x = findCenter(arr)
    y = [math.floor(len(arr)/2), math.floor(len(arr[0])/2)]
    di = x[0] - y[0]
    dj = x[1] - y[1]
    arr1 = np.zeros(arr.shape)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i + di >= 0 and i + di < len(arr):
                if j + dj >= 0 and j + dj < len(arr[i]):
                    arr1[i][j] = arr[i + di][j + dj]
                else:
                    continue
            else:
                continue
    img = Image.fromarray(arr1)
    return img

def clearFont(img):
    arr1 = np.asarray(img)
    arr = np.array(arr1)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 or i == len(arr) - 1:
                arr[i][j] = 2
                continue
            else:
                if j == 0 or j == len(arr[i]) - 1:
                    arr[i][j] = 2
                    continue
                else:
                    continue
    for i in range(1,len(arr)-1):
        for j in range(1, len(arr[i])-1):
            if arr[i][j] == 2 or arr[i][j] == 0:
                continue
            else:
                if arr[i][j-1] == 2 or arr[i][j+1] == 2:
                    arr[i][j] = 2
                else:
                    if arr[i-1][j] == 2 or arr[i+1][j] == 2:
                        arr[i][j] = 2
                    else:
                        if arr[i-1][j-1] == 2 or arr[i-1][j+1] == 2:
                            arr[i][j] = 2
                        else:
                            if arr[i+1][j-1] == 2 or arr[i+1][j+1] == 2:
                                arr[i][j] = 2
                            else:
                                continue
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                arr[i][j] = 0
            else:
                continue
    img = Image.fromarray(arr)
    return img

def addSpace(img, t):
    arr = np.asarray(img)
    arr1 = np.zeros((t + t + len(arr), t + t + len(arr[0])))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr1[i+t][j+t] = arr[i][j]
    img = Image.fromarray(arr1)
    return img

def conv1(pic, s = 0.9):
    img1 = Image.open(pic)
    img1 = img1.convert('L')
    arr = np.asarray(img1)
    delta = getAvarage(arr)
    img1 = img1.point(
        lambda x: 255 if x < s * delta else 0
    )
    img1 = reShape(img1,len(arr),len(arr[0]))
    return img1

def conv2(pic, s = 0.8):
    img1 = Image.open(pic)
    img1 = img1.convert('L')
    arr = np.asarray(img1)
    delta = getAvarage(arr)
    img1 = img1.point(
        lambda x: 255 if x > s * delta else 0
    )
    img1 = reShape(img1,len(arr),len(arr[0]))
    return img1

def conv3(pic, s = 1):
    img1 = Image.open(pic)
    red, green, blue = img1.split()
    zeroed_band = red.point(lambda _: 0)
    img1 = Image.merge(
        "RGB", (red, zeroed_band, zeroed_band)
    )
    img1 = img1.convert('L')
    arr = np.asarray(img1)
    delta = getAvarage(arr)
    img1 = img1.point(
        lambda x: 255 if x > s * delta else 0
    )
    img1 = reShape(img1, len(arr), len(arr[0]))
    return img1

def conv4(pic, s = 1):
    img1 = Image.open(pic)
    red, green, blue = img1.split()
    zeroed_band = red.point(lambda _: 0)
    img1 = Image.merge(
        "RGB", (red, zeroed_band, zeroed_band)
    )
    img1 = img1.convert('L')
    arr = np.asarray(img1)
    delta = getAvarage(arr)
    img1 = img1.point(
        lambda x: 255 if x < s * delta else 0
    )
    img1 = reShape(img1, len(arr), len(arr[0]))
    return img1

def conv5(pic, s = 1):
    img1 = Image.open(pic)
    red, green, blue = img1.split()
    zeroed_band = red.point(lambda _: 0)
    img1 = Image.merge(
        "RGB", (zeroed_band, zeroed_band, blue)
    )
    img1 = img1.convert('L')
    arr = np.asarray(img1)
    delta = getAvarage(arr)
    img1 = img1.point(
        lambda x: 255 if x < s * delta else 0
    )
    img1 = reShape(img1, len(arr), len(arr[0]))
    return img1

def conv6(pic, s = 1):
    img1 = Image.open(pic)
    red, green, blue = img1.split()
    zeroed_band = red.point(lambda _: 0)
    img1 = Image.merge(
        "RGB", (zeroed_band, zeroed_band, blue)
    )
    img1 = img1.convert('L')
    arr = np.asarray(img1)
    delta = getAvarage(arr)
    img1 = img1.point(
        lambda x: 255 if x > s * delta else 0
    )
    img1 = reShape(img1, len(arr), len(arr[0]))
    return img1

img1 = conv1('photo_2023-11-28_22-30-47.jpg')
img1 = clearFont(img1)
img1 = reShape(img1, 150,150)
img1 = centrizePic(img1)
img1 = centrizePic(img1)
img1 = addSpace(img1,40)
#img1.show()
img1 = img1.convert('RGB')
#img1.save('test1_4.jpg')

img2 = conv1('photo_2023-11-28_22-30-53.jpg', 1.05)
img2 = clearFont(img2)
img2 = reShape(img2, 150,150)
img2 = centrizePic(img2)
img2 = centrizePic(img2)
img2 = centrizePic(img2)
img2 = centrizePic(img2)
img2 = addSpace(img2,40)
#img2.show()
img2 = img2.convert('RGB')
#img2.save('test2_7.jpg')

img3 = conv2('photo_2023-11-28_22-30-59.jpg', 2.3)
img3 = clearFont(img3)
img3 = reShape(img3, 1000,1000)
img3 = img3.crop((200, 0, 900, 800))
img3 = addSpace(img3, 250)
img3 = reShape(img3, 150,150)
img3 = centrizePic(img3)
img3 = centrizePic(img3)
img3 = centrizePic(img3)
#img3.show()
img3 = img3.convert('RGB')
#img3.save('test3_5.jpg')

img4 = conv1('photo_2023-11-28_22-31-03.jpg', 0.3)
img4 = centrizePic(img4)
img4 = reShape(img4, 1000,1000)
img4 = img4.crop((250, 250, 750, 750))
img4 = centrizePic(img4)
#img4.show()
img4 = img4.convert('RGB')
#img4.save('test4_4.jpg')

img5 = conv2('photo1_2023-11-28_22-31-06.jpg', 1)
img5 = clearFont(img5)
img5 = reShape(img5, 1000,1000)
img5 = img5.crop((100, 100, 950, 900))
img5 = addSpace(img5,400)
#img5.show()
img5 = img5.convert('RGB')
#img5.save('test5_3.jpg')

img6 = conv4('photo_2023-11-28_22-31-13.jpg', 0.8)
img6 = addSpace(img6, 300)
#img6.show()
img6 = img6.convert('RGB')
#img6.save('test6_5.jpg')

img7 = conv5('photo_2023-12-02_19-47-36.jpg', 0.8)
img7 = reShape(img7, 1000,1000)
img71 = img7.crop((0,0,350,1000))
img71 = addSpace(img71,200)
img72 = img7.crop((350,0,1000,1000))
img72 = addSpace(img72,200)
#img71.show()
#img72.show()
img71 = img71.convert('RGB')
img72 = img72.convert('RGB')
#img71.save('test7_1.jpg')
#img72.save('test8_2.jpg')

img8 = conv2('photo_2023-12-02_19-48-05.jpg',5)
img81 = img8.crop((290,350,480,900))
img82 = img8.crop((490,340,630,850))
img83 = img8.crop((670,300,800,820))
img84 = img8.crop((830,260,980,750))
img81 = addSpace(img81, 60)
img82 = addSpace(img82, 60)
img83 = addSpace(img83, 60)
img84 = addSpace(img84, 60)
#img81.show()
#img82.show()
#img83.show()
#img84.show()
img81 = img81.convert('RGB')
img82 = img82.convert('RGB')
img83 = img83.convert('RGB')
img84 = img84.convert('RGB')
#img81.save('test9_2.jpg')
#img82.save('test10_0.jpg')
#img83.save('test11_5.jpg')
#img84.save('test12_8.jpg')