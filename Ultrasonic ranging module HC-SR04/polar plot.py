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
        try:
            val = int(ser.readline().decode("utf-8").strip())  # получаемое значение
            pos = int(ser.readline().decode("utf-8").strip())
            print('Расстояние: {}. Угол: {}'.format(val, pos))
        except ValueError:
            print(ser)
    if 0 < val < 500:
        prevX, prevY = pos, Y
        X = pos
        Y = val

        # TODO подправить паузу
        plt.pause(.001)  # пауза между выводами
        ax.scatter(radians(X), Y)
        # plt.plot([radians(prevX), radians(X)], [prevY, Y])
plt.show()
