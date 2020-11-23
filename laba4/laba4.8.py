"""8. Сформувати сигнал синусоїди частоти 20.5 Гц амплітуди 1 В та тривалості 1 сек. для частоти дискретизації 1000
Гц. Отримати амплітудний спектр заданого сигналу. Дописати в кінці сигналу нульові відліки (10, 100, 1000 та 10000
відліків), отримуючи для кожного сигналу його амплітудний спектр. На графік кожного разу виводити спектр за допомогою
функції stem в межах від 19 до 22 Гц. Зробити висновки щодо впливу доповнення сигналу нулями на роздільну здатність в
частотній області та на якість визначення наявності синусоїдального коливання за спектральними характеристиками. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import pi, sin

sample_rate = 1000
duration = 1
amplitude = 1
frequency1 = 20.5
null = [np.zeros(0), np.zeros(10), np.zeros(100), np.zeros(1000), np.zeros(10000)]
x_label = ['Час, с', 'Частота, Гц']
title = ['Сигнал', 'Амплітудний спектр сигналу']

fig, axes = plt.subplots(len(null), 2, constrained_layout=True)
fig.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
    frequency = np.linspace(0, sample_rate, duration * sample_rate)
    signal = amplitude * sin(2 * pi * frequency1 * time)
    x = np.append(signal, null[i])
    y = 2 * np.abs(fft(x) / len(x))
    time_new = np.linspace(0, len(x) / sample_rate, len(x), endpoint=False)
    frequency_new = np.linspace(0, sample_rate, len(x), endpoint=False)

    ax[0].plot(time_new, x)
    ax[1].stem(frequency_new, y)
    ax[1].set_xlim(19, 22)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(f"{title[j]} із частотою 20.5 Гц ({len(null[i])} нульових відліків)")
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()
