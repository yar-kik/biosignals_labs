"""2. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 128 Гц. Сформувати сигнали ділянки
синусоїди частотою 2 та 2.5 Гц. Побудувати амплітудний спектр сигналів без використання віконної функції та з
використанням першого вікна згідно варіанту. Тривалість вікна обрати рівною тривалості сигналів. Порівняти з
результатами п. 1 лабораторної роботи зі спектрального аналізу. Зробити висновки щодо спотворення спектрів та
доцільності використання віконної обробки. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import flattop

duration = 1
sample_rate = 128
time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
freq = np.linspace(0, sample_rate, duration * sample_rate)

frequency = [2, 2.5]

fig, axes = plt.subplots(2, 3, constrained_layout=True)
for i, ax in enumerate(axes):
    x = np.sin(2 * np.pi * frequency[i] * time)
    y = 2 * np.abs(fft(x) / len(x))
    z = 2 * np.abs(fft(x * flattop(len(x))) / len(x))
    ax[0].plot(time, x)
    ax[1].stem(freq, y)
    ax[2].stem(freq, z)
    ax[2].set_xlim(0, sample_rate // 2)
    ax[1].set_xlim(0, sample_rate // 2)
plt.show()


