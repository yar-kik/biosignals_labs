"""7. Сформувати сигнал синусоїди частоти 20 Гц амплітуди 1 В та тривалості 0.5 сек. для частоти дискретизації 128
Гц. Додати до цього сигналу шумову складову амплітуди 10 В  з нульовим середнім значенням (функція randn). Отримати
амплітудний спектр заданого сигналу.
7.1. Збільшувати тривалість зашумленого сигналу (1, 10, 100, 1000 сек.),
отримуючи для кожного сигналу його амплітудний спектр. Побудувати за допомогою функції plot графіки сигналів та їх
амплітудних спектрів, зробити висновки щодо впливу тривалості сигналу на роздільну здатність в частотній області та
на якість визначення наявності синусоїдального коливання в шумі за спектральними характеристиками.
7.2. Збільшувати частоту дискретизації зашумленого сигналу тривалості 0.5 сек (1280, 12800, 128000 Гц),
отримуючи для кожного сигналу його амплітудний спектр. На графік кожного разу виводити спектр в межах від 0 до 100 Гц.
Побудувати за допомогою функції plot графіки сигналів та їх амплітудних спектрів, зробити висновки щодо впливу частоти
дискретизації сигналу на роздільну здатність в частотній області та на якість визначення наявності синусоїдального
коливання в шумі за спектральними характеристиками. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import pi, sin

sample_rate = 128
duration = .5
signal_amplitude = 1
noise_amplitude = 10
frequency1 = 20

time = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
frequency = np.linspace(0, sample_rate, int(duration * sample_rate))
signal = signal_amplitude * sin(2 * pi * frequency1 * time)
noise = noise_amplitude * np.random.rand(len(time))
x = signal + noise
# x = np.random.random(len(time))
y = 2 * np.abs(fft(x - np.mean(x)) / len(x))
# y = 2 * np.abs(fft(x) / len(x))


fig, axes = plt.subplots(2, constrained_layout=True)
fig.set_size_inches(8, 6)
axes[0].plot(time, x)
axes[1].stem(frequency, y)
axes[1].set_xlim(0, sample_rate / 2)
axes[0].set_xlabel('Час, с')
axes[1].set_xlabel('Частота, Гц')
axes[0].set_ylabel("Амплітуда, В")
axes[1].set_ylabel("Амплітуда, В")
axes[0].set_title("Частота")
axes[1].set_title("Спектр")
plt.show()

