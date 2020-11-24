"""2. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 128 Гц. Сформувати сигнали ділянки
синусоїди частотою 2 та 2.5 Гц. Побудувати амплітудний спектр сигналів без використання віконної функції та з
використанням першого вікна згідно варіанту. Тривалість вікна обрати рівною тривалості сигналів. Порівняти з
результатами п. 1 лабораторної роботи зі спектрального аналізу. Зробити висновки щодо спотворення спектрів та
доцільності використання віконної обробки. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import flattop

duration = 1
sample_rate = 128
time = np.arange(0, duration, 1 / sample_rate)
freq = np.arange(0, sample_rate, 1 / duration)

frequency = [2, 2.5]
title = [["Сигнал з частотою 2 Гц", "Сигнал з частотою 2.5 Гц"],
         ['Амплітудний спектр без віконної функції', 'Амплітудний спектр без віконної функції'],
         ['Амплітудний спектр із віконною функцією', 'Амплітудний спектр із віконною функцією']]
x_label = ["Час, с", "Частота, Гц", "Частота, Гц"]
figure, axes = plt.subplots(2, 3, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    x = np.sin(2 * np.pi * frequency[i] * time)
    y = 2 * np.abs(fft(x) / len(x))
    y_window = 2 * np.abs(fft(x * flattop(len(x))) / len(x))
    ax[0].plot(time, x)
    ax[1].stem(freq, y)
    ax[1].set_xlim(0, sample_rate / 2)
    ax[2].stem(freq, y_window)
    ax[2].set_xlim(0, sample_rate / 2)
    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[j][i])
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()


