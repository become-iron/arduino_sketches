# -*- coding: utf-8 -*-
import serial
import matplotlib.pyplot as plt
from math import radians


X = 0
Y = 0
prevX = 0
prevY = 0

ax = plt.subplot(111, projection='polar')

while True:
    with serial.Serial('COM7', 9600, timeout=1) as ser:
        val = int(ser.readline().decode("utf-8")[:-2])  # получаемое значение
        print(val)
    if val < 50:
        prevX, prevY = X, Y
        X, Y = X + 10, val

        # TODO подправить паузу
        plt.pause(.5)  # пауза между выводами
        ax.scatter(radians(X), Y)
        plt.plot([radians(prevX), radians(X)], [prevY, Y])
plt.show()
