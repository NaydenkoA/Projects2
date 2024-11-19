import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import os

def conv(name):
    img = Image.open(name)
    img = img.resize((28, 28))
    img = img.convert('L')
    i = np.asarray(img)
    return i

def answer(arr):
    maxI = 0
    for i in range(1,len(arr)):
        if arr[i]>arr[maxI]:
            maxI = i
    print(maxI)

arr_name = []
for i in os.listdir():
    if i[len(i)-1] != 'g' or i[0] != 't':
        continue
    arr_name.append(i)
print(arr_name)

arr = [conv(arr_name[0])]
for i in range(1,len(arr_name)):
    arr.append(conv(arr_name[i]))
arr = np.array(arr)

n = 10
input_shape = (28, 28, 1)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float64") / 255
x_test = x_test.astype("float64") / 255
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
y_train = keras.utils.to_categorical(y_train, n)
y_test = keras.utils.to_categorical(y_test, n)


model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(n, activation="softmax"),
    ]
)

model1 = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(n, activation="softmax"),
    ]
)

bs = 128
ep = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=bs, epochs=ep, validation_split=0.3)

model1.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model1.fit(x_train, y_train, batch_size=bs, epochs=ep, validation_split=0.3)

answ1 = model1(arr)
answ = model(arr)

for i in range(len(answ)):
    print(' ')
    print(arr_name[i])
    print('conv')
    answer(answ[i])
    print('perceptron')
    answer(answ1[i])