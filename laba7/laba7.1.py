"""1. Сформувати вектор відліків часу тривалістю 1 с для частоти
дискретизації 256 Гц. Сформувати сигнал випадкового білого гаусівського
шуму (функція randn). Розрахувати та побудувати графік автокореляційної
функції. Зробити висновки щодо характеру АКФ для шума."""

import numpy as np
import matplotlib.pyplot as plt

duration = 1
sample_rate = 256
t = np.linspace(0, duration, duration * sample_rate)
x = np.random.randn(len(t))
y = np.correlate(x, x, mode="full") / len(x)  # нормування значень

plt.figure(num=1, figsize=(8, 6))
plt.stem(y)
plt.title("Графік автокореляційної функції", fontsize=14)
plt.xlabel("Лаг", fontsize=10)  # лаг - величина зсуву в часі
plt.ylabel("Автокореляція", fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
