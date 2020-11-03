"""8. Сформувати сигнал синусоїди частоти 20.5 Гц амплітуди 1 В та тривалості 1 сек. для частоти дискретизації 1000
Гц. Отримати амплітудний спектр заданого сигналу. Дописати в кінці сигналу нульові відліки (10, 100, 1000 та 10000
відліків), отримуючи для кожного сигналу його амплітудний спектр. На графік кожного разу виводити спектр за допомогою
функції stem в межах від 19 до 22 Гц. Зробити висновки щодо впливу доповнення сигналу нулями на роздільну здатність в
частотній області та на якість визначення наявності синусоїдального коливання за спектральними характеристиками. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import pi, sin

sample_rate = 1000
duration = 1
amplitude = 1
frequency1 = 20.5


null = [np.zeros(0), np.zeros(10), np.zeros(100), np.zeros(1000), np.zeros(10000)]
for i in range(len(null)):
    time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
    frequency = np.linspace(0, sample_rate, duration * sample_rate)
    signal = amplitude * sin(2 * pi * frequency1 * time)
    x = np.append(signal, null[i])
    y = 2 * np.abs(fft(x) / len(x))
    time_new = np.linspace(0, len(x) / sample_rate, len(x), endpoint=False)
    frequency_new = np.linspace(0, sample_rate, len(x), endpoint=False)
    fig, axes = plt.subplots(2, constrained_layout=True)
    fig.set_size_inches(8, 6)
    axes[0].plot(time_new, x)
    axes[1].stem(frequency_new, y)
    axes[1].set_xlim(19, 22)
    axes[0].set_xlabel('Час, с')
    axes[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    # ax[0].set_title(f"Частота {f[i]} Гц")
    axes[1].set_title("Спектр")
    plt.show()
