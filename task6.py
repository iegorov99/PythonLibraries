import matplotlib.pyplot as plt
import math as m
import numpy as np
import pandas as pd

# Задача 1:
# Придумайте сложную алгебраическую функцию, там могут быть синусы и косинусы, возведения в степень и деления, всё, что вашей душе угодно. 
# Напишите её с помощью def, чтобы она брала на вход x, а возвращала результат.
# Сгенерируйте X- координаты точки с помощью np.linspace(), а Y получите, положив X в вашу функцию. 
# Нарисуйте график, подпишите оси и сделайте подпись всей картинки(титульник).
# Сделайте так, чтобы на вашем графике были клеточки, график был пунктиром и зелёного цвета, а ещё полупрозрачным, и, чтобы к нему была подпись “Вот такая моя функция”.

# def func(x):
#     return m.cos(m.sin(x*x)*m.log(m.sqrt(x**x)))*10

# x = np.linspace(1, 10, 100)


# Задача 2:
# Сгенерируйте данные следующим образом.
# X = np.random.normal(0, 1, 3000)
# Y = np.random.normal(3, 4, 3000)
# Отобразите точки с помощью plt.scatter(). 
# Подпишите оси и график, сделайте клеточки, укажите какой-нибудь размер точек, цвет и добавьте аргумент maker=’<’. 
# Вместо < можете указать что-то своё. Укажите прозрачность, чтобы можно было увидеть, где много точек в одном месте, а где мало.

# x = np.random.normal(0, 1, 3000)
# y = np.random.normal(3, 4, 3000)

# data = plt.scatter(x, y, color= 'green', s = 50, alpha = 0.5)
# plt.title('График')
# plt.xlabel('Иксы')
# plt.ylabel('Игрики')
# plt.show()


# Задача 3.
# Возможные результаты забега школьников на 100 метров можно сгенерировать следующим образом:
# data = np.random.normal(16, 2, 1000)
# Постройте гистограмму красного цвета с полупрозрачными столбиками. Какие выводы можно сделать о результатах по ней?

data = np.random.normal(16, 2, 1000)
plt.hist(data, bins= 300,color = 'red', alpha = 0.5, rwidth=1)
plt.show()