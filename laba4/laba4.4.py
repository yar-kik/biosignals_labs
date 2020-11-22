"""4. Сформувати вектор відліків часу тривалістю 3 с для частоти дискретизації 512 Гц. Сформувати сигнал
послідовності прямокутних імпульсів з частотою 10 та 100 Гц. Побудувати за допомогою функції plot графіки сигналів та
їх амплітудних спектрів, зробити висновки. Графіки будувати для таких частот, щоб було видно особливості спектру
(вивести на графік частину спектру на нижніх частотах). """

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.fft import fft
from numpy import pi

sample_rate = 512
duration = 3
frequency1 = 10
frequency2 = 100
t = np.linspace(0, duration, duration * sample_rate)
f = np.linspace(0, sample_rate, duration * sample_rate)
x1 = square(2 * pi * frequency1 * t)
x2 = square(2 * pi * frequency2 * t)

y1 = 2 * np.abs(fft(x1) / len(x1))
y2 = 2 * np.abs(fft(x2) / len(x2))

frequency = [frequency1, frequency2]
x12 = [x1, x2]
y12 = [y1, y2]

x_label = ['Час, с', 'Частота, Гц', 'Частота, Гц']
title = [['Сигнал прямокутних імпульсів частоти 10 Гц', 'Сигнал прямокутних імпульсів частоти 100 Гц'],
         ['Спектр сигналу', 'Спектр сигналу'],
         ['Спектр сигналу на нижніх частотах', 'Спектр сигналу на нижніх частотах']]
fig, axes = plt.subplots(2, 3, constrained_layout=True)
fig.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    ax[0].plot(t, x12[i])
    ax[1].stem(f, y12[i])
    ax[1].set_xlim(0, sample_rate / 2)
    ax[2].stem(f, y12[i])
    ax[2].set_xlim(0, sample_rate / 32)
    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[j][i])
        ax[j].set_ylabel("Амплітуда")
plt.show()