"""5. Сформувати вектор відліків часу тривалістю 30 с для частоти дискретизації 512 Гц. Сформувати сигнал одиночного
прямокутного імпульсу для тривалості імпульсу 0.1, 1, 10 сек. (для величин зсуву відносно початку відліку часу 0 та 5
с). Побудувати за допомогою функції plot графіки цих 6 сигналів та їх амплітудних і фазових спектрів (функція angle),
зробити висновки. Графіки будувати для таких частот, щоб було видно особливості спектру. """
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.fft import fft
from numpy import pi


def single_square(t: np.array, tau: Union[int, float]):
    """"""
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
time = np.linspace(0, duration, duration * sample_rate)
frequency = np.linspace(0, sample_rate, duration * sample_rate)


fig, axes = plt.subplots(3, 3, constrained_layout=True)
fig.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    x = single_square(time * time_shift, pulse_durations[i])
    y = 2 * np.abs(fft(x) / len(x))
    phase = np.unwrap(np.angle(2 * fft(x) / len(x)))
    ax[0].plot(time, x)
    ax[1].stem(frequency, y)
    ax[1].set_xlim(0, sample_rate / 2)
    ax[0].set_xlabel('Час, с')
    ax[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    # ax[0].set_title(f"Частота {f[i]} Гц")
    ax[1].set_title("Спектр")
    ax[2].stem(frequency, phase)
    ax[2].set_xlim(0, sample_rate / 2)
plt.show()

fig, axes = plt.subplots(3, 3, constrained_layout=True)
fig.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    x = single_square(time - time_shift, pulse_durations[i])
    y = np.abs(2 * fft(x) / len(x))
    phase = np.unwrap(np.angle(2 * fft(x) / len(x)))
    ax[0].plot(time, x)
    ax[1].stem(frequency, y)
    ax[1].set_xlim(0, sample_rate / 2)
    ax[0].set_xlabel('Час, с')
    ax[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    # ax[0].set_title(f"Частота {f[i]} Гц")
    ax[1].set_title("Спектр")
    ax[2].stem(frequency, phase)
    ax[2].set_xlim(0, sample_rate / 2)
plt.show()