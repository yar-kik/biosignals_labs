"""4. Для сигналів з п. 2 лабораторної роботи про спектральний аналіз побудувати спектрограми:
– з вікном тривалості 0.1 с та 2 с (без перекриття);
– з вікном тривалості 1 с з перекриттям 50%.
Застосувати функцію colorbar для візуалізації значень спектрограми. Зробити висновки щодо відображення часових
властивостей сигналів у спектрограмі. Порівняти інформативність спектрограм та спектрів за Фурьє.
*Побудувати тривимірні графіки двох різних спектрограм з отриманих.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import flattop

duration = 10
sample_rate = 256
frequency1 = 10
frequency2 = 100


t1 = np.arange(0, duration, 1 / sample_rate)
t2 = np.arange(0, 2 * duration, 1 / sample_rate)
f1 = np.arange(0, sample_rate, 1 / duration)
f2 = np.arange(0, sample_rate, 1 / (2 * duration))


s1 = np.sin(2 * np.pi * frequency1 * t1)
s2 = np.sin(2 * np.pi * frequency2 * t1)

x1 = s1 + s2
x2 = np.append(2 * s1, 2 * s2)
x3 = np.append(2 * s2, 2 * s1)


signals = [x1, x2, x3]
times = [t1, t2, t2]
frequency = [f1, f2, f2]

window_duration1 = .1
window_duration2 = 2
window_duration3 = 1

NFFT1 = int(window_duration1 * sample_rate)
NFFT2 = int(window_duration2 * sample_rate)
NFFT3 = int(window_duration3 * sample_rate)

NFTT = [NFFT1, NFFT2]

window1 = flattop(NFFT1)
window2 = flattop(NFFT2)
window3 = flattop(NFFT3)
for i in range(len(signals)):
    fig, axes = plt.subplots(2, constrained_layout=True)
    axes[0].plot(times[i], signals[i])
    axes[1].specgram(signals[i], Fs=sample_rate, NFFT=NFFT3, noverlap=NFFT3//2, window=window3)
    plt.show()
