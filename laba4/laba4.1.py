import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import sin, pi

sample_rate = 128
duration = 1
t = np.arange(0, duration, 1 / sample_rate)
f = np.arange(0, sample_rate, 1 / duration)
frequency = np.array([2, 2.5, 40, 100, 600])

x_label = ['Час, с', 'Частота, Гц']
title = ['Сигнал', 'Спектр сигналу']

figure, axes = plt.subplots(len(frequency), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    x = sin(2 * pi * frequency[i] * t)
    y = 2 * abs(fft(x) / len(t))

    ax[0].plot(t, x)
    ax[1].stem(f, y)
    ax[1].set_xlim(0, sample_rate / 2)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(f"{title[j]} (частота {frequency[i]} Гц)")
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()
