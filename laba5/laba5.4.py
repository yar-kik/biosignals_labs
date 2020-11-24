"""4. Для сигналів з п. 2 лабораторної роботи про спектральний аналіз побудувати спектрограми:
– з вікном тривалості 0.1 с та 2 с (без перекриття);
– з вікном тривалості 1 с з перекриттям 50%.
Застосувати функцію colorbar для візуалізації значень спектрограми. Зробити висновки щодо відображення часових
властивостей сигналів у спектрограмі. Порівняти інформативність спектрограм та спектрів за Фурьє.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

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

window_duration1 = .1
window_duration2 = 2
window_duration3 = 1

x_label = ["Час, с", "Час, с"]
y_label = ["Амплітуда", "Частота, Гц"]
title = [[f'Сигнал $S_1$+$S_2$', "Спектрограма (тривалість вікна 0.1с)"],
         [f"Сигнал 2*$S_1$, 2*$S_2$", "Спектрограма (тривалість вікна 0.1с)"],
         [f"Сигнал 2*$S_2$, 2*$S_1$", "Спектрограма (тривалість вікна 0.1с)"]]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    f, t, y = spectrogram(x[i], fs=sample_rate, window='flattop', noverlap=0,
                          nperseg=int(window_duration1 * sample_rate))
    ax[0].plot(time[i], x[i])
    pcm = ax[1].pcolormesh(t, f, y, shading='gouraud')
    figure.colorbar(pcm, ax=ax[1])
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel(y_label[j])
plt.show()


title = [[f'Сигнал $S_1$+$S_2$', "Спектрограма (тривалість вікна 2с)"],
         [f"Сигнал 2*$S_1$, 2*$S_2$", "Спектрограма (тривалість вікна 2с)"],
         [f"Сигнал 2*$S_2$, 2*$S_1$", "Спектрограма (тривалість вікна 2с)"]]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    f, t, y = spectrogram(x[i], fs=sample_rate, window='flattop', noverlap=0,
                          nperseg=int(window_duration2 * sample_rate))
    ax[0].plot(time[i], x[i])
    pcm = ax[1].pcolormesh(t, f, y, shading='gouraud')
    figure.colorbar(pcm, ax=ax[1])
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel(y_label[j])
plt.show()

title = [[f'Сигнал $S_1$+$S_2$', "Спектрограма (тривалість вікна 1с, з перекриттям 50%)"],
         [f"Сигнал 2*$S_1$, 2*$S_2$", "Спектрограма (тривалість вікна 1с, з перекриттям 50%)"],
         [f"Сигнал 2*$S_2$, 2*$S_1$", "Спектрограма (тривалість вікна 1с, з перекриттям 50%)"]]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    f, t, y = spectrogram(x[i], fs=sample_rate, window='flattop',
                          noverlap=int(window_duration3 * sample_rate * .5),
                          nperseg=int(window_duration3 * sample_rate))
    ax[0].plot(time[i], x[i])
    pcm = ax[1].pcolormesh(t, f, y, shading='gouraud')
    figure.colorbar(pcm, ax=ax[1])
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel(y_label[j])
plt.show()