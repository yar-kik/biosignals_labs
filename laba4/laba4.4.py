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
f = [frequency1, frequency2]
time = np.linspace(0, duration, duration * sample_rate)
frequency = np.linspace(0, sample_rate, duration * sample_rate)
x1 = square(2 * pi * frequency1 * time)
x2 = square(2 * pi * frequency2 * time)
x12 = [x1, x2]

y1 = 2 * np.abs(fft(x1) / len(x1))
y2 = 2 * np.abs(fft(x2) / len(x2))
y12 = [y1, y2]


fig, axes = plt.subplots(2, 2, constrained_layout=True)
fig.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax[0].plot(time, x12[i], linewidth=.7)
    ax[1].stem(frequency, y12[i])
    ax[1].set_xlim(0, sample_rate / 2)
    ax[0].set_xlabel('Час, с')
    ax[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    ax[0].set_title(f"Частота {f[i]} Гц")
    ax[1].set_title("Спектр")
plt.show()