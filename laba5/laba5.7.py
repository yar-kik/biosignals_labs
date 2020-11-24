"""*. Сформувати вектор відліків часу тривалістю 10 с для частоти дискретизації 128 Гц. Сформувати сигнал
послідовності прямокутних імпульсів. Сформувати відліки одної віконної функції тривалості 0.2 секунди та 2 секунди.
Побудувати спектрограми сигналу. Побудувати тривимірні графіки модуля спектральної функції. """
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import flattop
from scipy.signal import square

duration = 10
sample_rate = 128
time = np.linspace(0, duration, sample_rate * duration, endpoint=False)
freq = np.linspace(0, sample_rate, sample_rate * duration)
frequency = 40

time_shift = 10
window_duration1 = .2
window_duration2 = 2

NFFT1 = int(window_duration1 * sample_rate)
NFFT2 = int(window_duration2 * sample_rate)

window1 = flattop(NFFT1)
window2 = flattop(NFFT2)

x = square(2 * np.pi * time * frequency)
X, Y = np.meshgrid(time, x)
z = np.sin(np.sqrt(X ** 2 + Y ** 2))
ax = plt.axes(projection='3d')
ax.plot_surface(time, x, z)
plt.show()
