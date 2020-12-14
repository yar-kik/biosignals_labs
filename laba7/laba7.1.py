"""1. Сформувати вектор відліків часу тривалістю 1 с для частоти
дискретизації 256 Гц. Сформувати сигнал випадкового білого гаусівського
шуму (функція randn). Розрахувати та побудувати графік автокореляційної
функції. Зробити висновки щодо характеру АКФ для шума."""

import numpy as np
import matplotlib.pyplot as plt

duration = 1
sample_rate = 256
t = np.linspace(0, duration, duration * sample_rate)
x = np.random.randn(sample_rate * duration)
y = np.correlate(x, x, mode="full")

plt.figure(num=1, figsize=(8, 6))
plt.stem(y)
plt.title("", fontsize=14)
plt.xlabel("", fontsize=10)
plt.ylabel("", fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
