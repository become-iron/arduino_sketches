# -*- coding: utf-8 -*-
import serial
import matplotlib.pyplot as plt


X = 0
Y = 0
prevX = 0
prevY = 0

ser = serial.Serial('/dev/ttyUSB0')
plt.scatter(X, Y)

while True:
    with serial.Serial('COM7', 9600, timeout=1) as ser:
        val = int(ser.readline().decode("utf-8").strip())
        print(val)
    if val < 50:
        prevX, prevY = X, Y
        X += 10
        Y = val

        # TODO подправить паузу
        plt.pause(.5)  # пауза между выводами
        plt.scatter(X, Y)
        plt.plot([prevX, X], [prevY, Y])
plt.show()
