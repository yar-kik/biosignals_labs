import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import pi, sin

sample_rate = 128
duration = [1, 10, 100, 1000]
signal_amplitude = 1
noise_amplitude = 10
frequency1 = 20

# x = np.random.random(len(time))


for i in range(len(duration)):
    time = np.linspace(0, duration[i], duration[i] * sample_rate, endpoint=False)
    frequency = np.linspace(0, sample_rate, duration[i] * sample_rate)
    signal = signal_amplitude * sin(2 * pi * frequency1 * time)
    noise = noise_amplitude * np.random.rand(len(time))
    x = signal + noise
    y = 2 * np.abs(fft(x) / len(x))

    fig, axes = plt.subplots(2, constrained_layout=True)
    fig.set_size_inches(8, 6)
    axes[0].plot(time, x, linewidth=.7)
    axes[1].stem(frequency, y)
    axes[1].set_xlim(0, sample_rate / 2)
    axes[0].set_xlabel('Час, с')
    axes[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    # ax[0].set_title(f"Частота {f[i]} Гц")
    axes[1].set_title("Спектр")
    plt.show()

