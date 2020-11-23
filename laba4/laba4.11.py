"""11. Побудувати функцію, яка дозволяє розрахувати та побудувати  амплітудний та фазовий спектр фрагменту довільного
сигналу. """
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.io import loadmat


def build_amplitude_and_phase(x: np.array, fs: Union[int, float]) -> None:
    """
    Функція для побудови графіка сигналу, його амплітудного та фазового спектру
    """
    duration = len(x) / fs
    time = np.linspace(0, duration, len(x))
    frequency = np.linspace(0, fs, len(x))
    transform = fft(signal - np.mean(signal))
    amplitude = 2 * np.abs(transform / len(signal))
    phase = np.unwrap(np.angle(transform))

    x_label = ['Час, с', 'Частота, Гц', 'Частота, Гц']
    y_label = ["Амплітуда", "Амплітуда", "Фаза, радіани"]
    title = ['Сигнал', "Амплітудний спектр", "Фазовий спектр"]

    fig, ax = plt.subplots(3, constrained_layout=True)
    fig.set_size_inches(12, 6)
    ax[0].plot(time, x)
    ax[1].stem(frequency, amplitude)
    ax[1].set_xlim(0, fs / 2)
    ax[2].stem(frequency, phase)
    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[j])
        ax[j].set_ylabel(y_label[j])
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
    plt.show()


ekg_normal = np.load('../data/norm/1600715877.npz')
sample_rate = ekg_normal['fs']
signal = ekg_normal['signal']

build_amplitude_and_phase(signal, sample_rate)