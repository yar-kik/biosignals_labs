import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import pi, sin

sample_rate = [128, 1280, 12800, 128000]
duration = .5
signal_amplitude = 1
noise_amplitude = 10
frequency1 = 20

# x = np.random.random(len(time))


for i in range(len(sample_rate)):
    time = np.linspace(0, duration, int(duration * sample_rate[i]), endpoint=False)
    # time = np.arange(0, duration, 1 / sample_rate[i])
    frequency = np.linspace(0, sample_rate[i], int(duration * sample_rate[i]))
    signal = signal_amplitude * sin(2 * pi * frequency1 * time)
    noise = noise_amplitude * np.random.rand(len(time))
    x = signal + noise
    y = 2 * np.abs(fft(x) / len(x))

    fig, axes = plt.subplots(2, constrained_layout=True)
    fig.set_size_inches(8, 6)
    axes[0].plot(time, x, linewidth=.7)
    axes[1].stem(frequency, y)
    axes[1].set_xlim(0, 100)
    axes[0].set_xlabel('Час, с')
    axes[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    # ax[0].set_title(f"Частота {f[i]} Гц")
    axes[1].set_title("Спектр")
    plt.show()
