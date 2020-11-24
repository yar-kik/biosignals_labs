"""5. Для сигналів з п. 3 лабораторної роботи про спектральний аналіз побудувати спектрограми сигналу з використанням
вікна, тривалість і перекриття якого підібрані оптимально для визначення моменту розриву в сигналі. Обгрунтувати свій
вибір та зробити висновки. """

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, pi
from scipy.signal import spectrogram

sample_rate = 128
duration = 3
frequency = 20

time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
x1 = sin(2 * pi * frequency * time)
x2 = np.copy(x1)
breaking1 = round(1.05 * sample_rate)
breaking2 = 2 * sample_rate

x1[breaking1:breaking1 + 10] = 0
x2[breaking2:breaking2 + 10] = 0
x = [x1, x2]

window_duration = .05
overlap = .9

x_label = ["Час, с", "Час, с"]
y_label = ["Амплітуда", "Частота, Гц"]
title = [['Сигнал із розривом в момент часу 1.05с', "Спектрограма"],
         ["Сигнал із розривом в момент часу 2.0с", "Спектрограма"]]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    f, t, y = spectrogram(x[i], fs=sample_rate, window='flattop',
                          noverlap=int(window_duration * sample_rate * overlap),
                          nperseg=int(window_duration * sample_rate))
    ax[0].plot(time, x[i])
    pcm = ax[1].pcolormesh(t, f, y, shading='gouraud')
    figure.colorbar(pcm, ax=ax[1])
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel(y_label[j])
plt.show()
