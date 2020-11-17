"""3. Сформувати вектор відліків часу тривалістю 15 с для частоти дискретизації 128 Гц.
Сформувати сигнали:
3.1. синусоїди частотою 40 Гц;
3.2. прямокутного імпульсу ширини 1 с в момент часу 10 с;
3.3. випадкового сигналу;
3.4.суми сигналів 3.1 – 3.3.
Побудувати спектрограми сигналів за допомогою першого вікна згідно варіанту тривалістю 0.2 с
без використання перекриття вікон. Зробити висновки щодо вигляду спектрограм та відповідності часових, спектральних
та спектрально-часових властивостей сигналів. """
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import flattop


def single_square(t: np.array, tau: Union[int, float]):
    """"""
    x = np.zeros(len(t))
    for k, tk in enumerate(t):
        if np.abs(tk) > tau/2:
            x[k] = 0
        else:
            x[k] = 1
    return x


duration = 15
sample_rate = 128
time = np.linspace(0, duration, sample_rate * duration, endpoint=False)
freq = np.linspace(0, sample_rate, sample_rate * duration)
frequency = 40
pulse_duration = 1
time_shift = 10
window_duration = .2
NFFT = int(window_duration * sample_rate)

window = flattop(NFFT)

x_sin = np.sin(2 * np.pi * frequency * time)
x_square = single_square(time - time_shift, pulse_duration)
x_random = np.random.random(len(time))
x_mixed = x_sin + x_square + x_random

x = [x_sin, x_square, x_random, x_mixed]
for j in range(len(x)):
    fig, axes = plt.subplots(2, constrained_layout=True)

    # for i, ax in enumerate(axes):
    axes[0].plot(time, x[j])
    axes[1].specgram(x[j], Fs=sample_rate, NFFT=NFFT, noverlap=0, window=window)
    plt.show()
