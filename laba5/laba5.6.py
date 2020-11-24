"""6. Побудувати функцію, яка будує графік зміни в часі середньої спектральної густини потужності в заданому
частотному діапазоні та часовому діапазоні для заданого сигналу. В якості параметрів функції передавати назву
сигналу, час t1, t2 та частоти f1, f2, а також інші необхідні параметри. """
from typing import Union, Iterable

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram


def spectral_density_delta(signal: np.array, sample_rate: int, f1: Union[int, float],
                           f2: Union[int, float], t1: Union[int, float],
                           t2: Union[int, float], *, overlap: float = 0,
                           window_duration: Union[int, float] = .1,
                           window: Union[str, Iterable[float]] = "flattop") -> None:
    """
    Функція для побудови графіку зміни середньої спектральної густини потужності в заданому частотному діапазоні
    та часовому діапазоні для заданого сигналу
    """
    if f1 > f2 or t1 > t2:
        raise ValueError("f1 should be less f2; t1 should be less t2")
    if t1 < 0 or t2 > len(x) / sample_rate:
        raise ValueError("Incorrect time limits")

    f, t, y = spectrogram(signal, fs=sample_rate, window=window,
                          noverlap=int(window_duration * sample_rate * overlap),
                          nperseg=int(window_duration * sample_rate))
    time = np.linspace(0, len(signal) / sample_rate, len(signal))
    freq1 = np.argmin(abs(f - f1))
    freq2 = np.argmin(abs(f - f2))
    time1 = np.argmin(abs(t - t1))
    time2 = np.argmin(abs(t - t2))
    y = np.mean(y[freq1:freq2, time1:time2], axis=0)
    x_label = ["Час, с", "Час, с"]
    y_label = ["Амплітуда", "Густина спектральноъ потужності"]
    title = ['Сигнал', "Графік зміни в часі середньої спектральної густини потужності"]

    figure, ax = plt.subplots(2, constrained_layout=True)
    figure.set_size_inches(12, 6)
    ax[0].plot(time, signal)
    ax[1].plot(t[time1:time2], y)
    ax[1].set_xlim(t1, t2)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[j])
        ax[j].set_ylabel(y_label[j])
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
    plt.show()


ekg_normal = np.load('../data/norm/1600715877.npz')
fs = ekg_normal['fs']
x = ekg_normal["signal"]
t1 = f1 = 0
t2 = 8
f2 = 15
wd = .5
spectral_density_delta(x, fs, f1, f2, t1, t2, window_duration=wd)

