from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt
import pywt


def build_scalogram(signal: Iterable[float, int],
                    scales: Iterable[float, int],
                    wavelet: str = 'gaus1') -> None:
    """
    Функція для побудови скейлограми довільного сигналу з
    використанням масштабуючих коефіцієнтів
    """
    figure, ax = plt.subplots(constrained_layout=True)
    figure.set_size_inches(12, 6)
    cwt_matrix, _ = pywt.cwt(signal, scales, wavelet)
    im = ax.imshow(abs(cwt_matrix), cmap='hot', aspect='auto',
                   extent=[t[0], t[-1], scales[-1], scales[0]])
    cbar = figure.colorbar(im)
    ax.invert_yaxis()
    ax.set_xlabel("Відліки")
    ax.set_title("Скейлограма")
    ax.set_ylabel("Масштаб")
    plt.show()


a = np.arange(1, 60)
duration = 10
sample_rate = 256
t = np.arange(0, duration, 1 / sample_rate)
x = 2 * np.sin(2 * np.pi * 5 * t) + t * np.sin(2 * np.pi * 2 * t)

build_scalogram(x, a)
