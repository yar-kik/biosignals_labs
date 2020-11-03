import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import sin, pi

sample_rate = 128
duration = 1

# time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
# f = np.linspace(0, sample_rate, duration * sample_rate)
time = np.arange(0, duration, 1 / sample_rate)
f = np.arange(0, sample_rate, 1 / duration)
frequency = np.array([2, 2.5, 40, 100, 600])

x = sin(2 * pi * np.outer(frequency, time))
# x = sin(2 * pi * frequency * time)
# print(sin(np.outer(frequency, time)))
y = 2 * np.abs(fft(x) / len(x))
figure, axes = plt.subplots(len(frequency), 2, constrained_layout=True)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax[0].plot(time, x[i])
    ax[1].stem(f, y[i])
    ax[0].set_xlabel('Час, с')
    ax[1].set_xlabel('Частота, Гц')
    ax[1].set_ylabel("Амплітуда, В")
    ax[0].set_title(f"Частота {frequency[i]} Гц")
    ax[1].set_title("Спектр")
    ax[1].minorticks_on()
    ax[1].grid(which='major', linewidth=1.2)
    ax[1].grid(which='minor', linewidth=.5)
    ax[1].set_xlim(0, sample_rate/2)
plt.show()
