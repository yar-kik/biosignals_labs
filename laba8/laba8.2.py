"""Сформувати вектор масштабних коефіцієнтів a=[.01:.02:.11 .2:.2:1 2:2:30].
Побудувати скейлограми сигналів лабораторної роботи по
спектрально-часовому аналізу. На основі аналізу скейлограм зробити
висновки щодо відповідності властивостей сигналів у часі, їх
відображення на скейлограмі. Порівняти відображення характеристик
сигналів на скейлограмі та спектрограмі, зробити висновки.
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt

a = [np.arange(.2, 1, .2), np.arange(2, 22, 2)]
a = np.hstack(a)
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

x_label = ["Час, с", "Час, с"]
y_label = ["Амплітуда", "Масштаб"]
title = [[f'Сигнал $S_1$+$S_2$', "Скейлограма"],
         [f"Сигнал 2*$S_1$, 2*$S_2$", "Скейлограма"],
         [f"Сигнал 2*$S_2$, 2*$S_1$", "Скейлограма"]]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    cwt_matrix, _ = pywt.cwt(x[i], a, "gaus1")
    ax[0].plot(time[i], x[i])
    im = ax[1].imshow(abs(cwt_matrix), cmap='hot', aspect='auto', extent=[t1[0], t1[-1], a[-1], a[0]])
    cbar = figure.colorbar(im, ax=ax[1])
    ax[1].invert_yaxis()
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel(y_label[j])
plt.show()