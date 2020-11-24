"""5. Сформувати вектор відліків часу тривалістю 30 с для частоти дискретизації 512 Гц. Сформувати сигнал одиночного
прямокутного імпульсу для тривалості імпульсу 0.1, 1, 10 сек. (для величин зсуву відносно початку відліку часу 0 та 5
с). Побудувати за допомогою функції plot графіки цих 6 сигналів та їх амплітудних і фазових спектрів (функція angle),
зробити висновки. Графіки будувати для таких частот, щоб було видно особливості спектру. """
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


def single_square(t: np.array, tau: Union[int, float]) -> np.array:
    """Функція для генерування одиночного прямокутного імпульсу"""
    x = np.zeros(len(t))
    for k, tk in enumerate(t):
        if np.abs(tk) > tau/2:
            x[k] = 0
        else:
            x[k] = 1
    return x


sample_rate = 512
duration = 30
time_shift = 5
pulse_durations = [.1, 1, 10]
x_lim = [200, 20, 2]
t = np.linspace(0, duration, duration * sample_rate)
f = np.linspace(0, sample_rate, duration * sample_rate)

x_label = ['Час, с', 'Частота, Гц', 'Частота, Гц']
y_label = ["Амплітуда", "Амплітуда", "Фаза, радіани"]
title = [['Сигнал одиночного прямокутного імпульсу 0.1с',
          'Сигнал одиночного прямокутного імпульсу 1с',
          'Сигнал одиночного прямокутного імпульсу 10с'],
         ['Амплітудний спектр', 'Амплітудний спектр', 'Амплітудний спектр'],
         ['Фазовий спектр', 'Фазовий спектр', 'Фазовий спектр']]
fig, axes = plt.subplots(3, 3, constrained_layout=True)
fig.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    x = single_square(t, pulse_durations[i])
    y = np.abs(fft(x) / len(x))
    phase = np.unwrap(np.angle(fft(x)))

    ax[0].plot(t, x)
    ax[1].stem(f, y)
    ax[2].stem(f, phase)
    ax[1].set_xlim(0, x_lim[i])
    ax[2].set_xlim(0, x_lim[i] * 2)
    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_ylabel(y_label[j])
        ax[j].set_title(title[j][i])
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()

fig, axes = plt.subplots(3, 3, constrained_layout=True)
fig.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    x = single_square(t - time_shift, pulse_durations[i])
    y = np.abs(2 * fft(x) / len(x))
    phase = np.unwrap(np.angle(fft(x)))
    ax[0].plot(t, x)
    ax[1].stem(f, y)
    ax[2].stem(f, phase)
    ax[1].set_xlim(0, x_lim[i])

    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[j][i])
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()