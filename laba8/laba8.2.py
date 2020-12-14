"""Сформувати вектор масштабних коефіцієнтів a=[.01:.02:.11 .2:.2:1 2:2:30].
Побудувати скейлограми сигналів лабораторної роботи по
спектрально-часовому аналізу. На основі аналізу скейлограм зробити
висновки щодо відповідності властивостей сигналів у часі, їх
відображення на скейлограмі. Порівняти відображення характеристик
сигналів на скейлограмі та спектрограмі, зробити висновки.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ricker, morlet2, cwt

a = [np.arange(.01, .11, 0.02), np.arange(.2, 1, .2), np.arange(2, 30, 2)]
a = np.hstack(a)
wavelet_width = 4
duration = 10
sample_rate = 256
frequency1 = 10
frequency2 = 100

t1 = np.arange(0, duration, 1 / sample_rate)
t2 = np.arange(0, 2 * duration, 1 / sample_rate)
s1 = np.sin(2 * np.pi * frequency1 * t1)
s2 = np.sin(2 * np.pi * frequency2 * t1)

x1 = s1 + s2
x2 = np.append(2 * s1, 2 * s2)
x3 = np.append(2 * s2, 2 * s1)

x = [x1, x2, x3]
time = [t1, t2, t2]
cwt_matrix = cwt(x2, ricker, a)
print(cwt_matrix.shape)
plt.figure(num=1, figsize=(8, 6))
# plt.pcolormesh(cwt_matrix, shading='gouraud')
# plt.plot(y)
plt.imshow(cwt_matrix, cmap='PRGn', aspect='auto',
           vmax=abs(cwt_matrix).max(), vmin=-abs(cwt_matrix).max())
plt.title("", fontsize=14)
plt.xlabel("", fontsize=10)
plt.ylabel("", fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()

# figure, axes = plt.subplots(2, constrained_layout=True)
# figure.set_size_inches(12, 6)
# for i, ax in enumerate(axes):
#     ax.plot(wavelets[i])
#     for j in range(len(wavelets)):
#         ax.set_xlabel("Номер відліку")
#         ax.set_title("")
#         ax.set_ylabel("Амплітуда")
#         ax.minorticks_on()
#         ax.grid(which='major', linewidth=1.2)
#         ax.grid(which='minor', linewidth=.5)
# plt.show()
