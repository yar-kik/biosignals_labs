"""10. Побудувати функцію для розрахунку та виводу на графік спектральної густини потужності сигналу, прочитаного з
файлу. В функцію передавати назву файлу з сигналом та інші необхідні дані. """
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.io import loadmat


def build_spectral_density(x: np.array, fs: Union[int, float]) -> None:
    """
    Функція для побудови графіка сигналу та його спектральної густини потужності
    """
    duration = len(x) / fs
    t = np.linspace(0, duration, len(x))
    f = np.linspace(0, fs, len(x))
    y = 2 * np.abs(fft(x) / len(x))
    power_spectral_density = y ** 2

    x_label = ['Час, с', 'Частота, Гц']
    y_label = ["Амплітуда", r"Спектральна густина"]
    title = ['Сигнал', 'Спектральна густина потужності сигналу']

    fig, ax = plt.subplots(2, constrained_layout=True)
    fig.set_size_inches(12, 6)
    ax[0].plot(t, x)
    ax[1].plot(f, power_spectral_density)
    ax[1].set_xlim(0, fs / 16)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[j])
        ax[j].set_ylabel(y_label[j])
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
    plt.show()


eeg_healthy = loadmat('../data/EEG_healthy/eeg_healthy_9.mat')
signal = eeg_healthy['sig'][0]
sample_rate = 256
build_spectral_density(signal, sample_rate)
