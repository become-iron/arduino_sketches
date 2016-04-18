# -*- coding: utf-8 -*-

"""
Считывание значений с ультразвукового датчика измерения расстояния HC-SR04, установленного
на сервопривод. Сервопривод совершает обороты на 180 градусов в течение заданного времени.
Затем по полученным данным происходит построение графика
"""

import serial
import matplotlib.pyplot as plt
from math import radians
from time import time

timeToWork = 1200  # время работы датчика

angle = 0  # угол
dist = 0  # расстояние

values = {degree: [] for degree in range(181)}

startTime = time()
finishTime = startTime + timeToWork

while time() <= finishTime:
    # TODO стоит добавить паузу?
    with serial.Serial('COM7', 9600, timeout=1) as ser:
        try:
            currDist = int(ser.readline().decode("utf-8").strip())  # получаемое значение
            currAngle = int(ser.readline().decode("utf-8").strip())
            print('Расстояние: {}. Угол: {}. Осталось: {}c'.format(currDist, currAngle, int(finishTime - time())))
        except ValueError:
            print('Ошибка: ', ser)

    if 0 < currDist < 500:
        angle = currAngle
        dist = currDist
        values[currAngle] = values[currAngle] + [currDist]


for key in values.keys():
    try:
        values.update({key: sum(values[key]) / len(values[key])})  # среднее арифм. значений для данного угла
    except ZeroDivisionError:  # е. для данного угла не получено значений
        del(values[key])

ax = plt.subplot(111, projection='polar')
for key in values.keys():
    ax.scatter(radians(key), values[key])
# plt.plot([radians(prevX), radians(X)], [prevY, Y])
plt.show()
