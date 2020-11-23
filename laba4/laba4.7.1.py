import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import pi, sin

sample_rate = 128
duration = [1, 10, 100, 1000]
signal_amplitude = 1
noise_amplitude = 10
frequency = 20

x_label = ['Час, с', 'Частота, Гц']
title = ['Сигнал', 'Амплітудний спектр сигналу']

fig, axes = plt.subplots(len(duration), 2, constrained_layout=True)
fig.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    t = np.arange(0, duration[i], 1 / sample_rate)
    f = np.arange(0, sample_rate, 1 / duration[i])
    signal = signal_amplitude * sin(2 * pi * frequency * t)
    noise = noise_amplitude * np.random.rand(len(t))
    x = signal + noise
    y = 2 * np.abs(fft(x - np.mean(x)) / len(x))

    ax[0].plot(t, x)
    ax[1].stem(f, y)
    ax[1].set_xlim(0, sample_rate / 2)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(f"{title[j]} тривалості {duration[i]} с")
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()


