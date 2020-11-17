"""5. Для сигналів з п. 3 лабораторної роботи про спектральний аналіз побудувати спектрограми сигналу з використанням
вікна, тривалість і перекриття якого підібрані оптимально для визначення моменту розриву в сигналі. Обгрунтувати свій
вибір та зробити висновки. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import sin, pi
from scipy.signal.windows import flattop

sample_rate = 128
duration = 3
frequency = 20

time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
x1 = sin(2 * pi * frequency * time)
x2 = sin(2 * pi * frequency * time)

breaking1 = round(1.05 * sample_rate)
breaking2 = 2 * sample_rate


x1[breaking1:breaking1 + 10] = 0
x2[breaking2:breaking2 + 10] = 0


x12 = [x1, x2]
window_duration = .05
NFFT = int(sample_rate * window_duration)

window = flattop(NFFT)


figure, axes = plt.subplots(2, 2, constrained_layout=True)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax[0].plot(time, x12[i])
    ax[1].specgram(x12[i], Fs=sample_rate, NFFT=NFFT, noverlap=NFFT//2, window=window)
    ax[0].set_xlabel('Час, с')
    ax[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    ax[0].set_title("Частота 20 Гц")
    ax[1].set_title("Спектр")
    # ax.minorticks_on()
    # ax.grid(which='major', linewidth=1.2)
    # ax.grid(which='minor', linewidth=.5)
plt.show()
