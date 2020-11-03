"""2. Сформувати вектор відліків часу тривалістю 10 с для частоти дискретизації 256 Гц. Сформувати сигнали ділянки
синусоїди частотою 10 Гц (S1) та 100 Гц (S2). Сформувати на їх основі три сигнали:
2.1. сигнал (тривалістю 10 с), що дорівнює сумі цих двох сигналів;
2.2. сигнал, який спочатку містить сигнал 2*S1, а потім сигнал 2*S2 (матиме тривалість 20 секунд);
2.3. сигнал, який спочатку містить сигнал 2*S2, а потім сигнал 2*S1 (матиме тривалість 20
секунд).
Побудувати графіки сигналів п. 2.1-2.3 (функція plot) та їх амплітудних спектрів (функція stem). Зробити
висновки щодо можливості розрізнити коливання, присутні у сигналі, по їх спектральному складу, а також щодо
відповідності властивостей сигналів у часі та їх спектрів. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import sin, pi


duration = 10
sample_rate = 256
frequency1 = 10
frequency2 = 100

# time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
# f = np.linspace(0, sample_rate, duration * sample_rate)
# frequency = np.array([2, 2.5, 40, 100, 600])
t1 = np.arange(0, duration, 1 / sample_rate)
t2 = np.arange(0, 2 * duration, 1 / sample_rate)
f1 = np.arange(0, sample_rate, 1 / duration)
f2 = np.arange(0, sample_rate, 1 / (2 * duration))


s1 = sin(2 * pi * frequency1 * t1)
s2 = sin(2 * pi * frequency2 * t1)

x1 = s1 + s2
x2 = np.append(2 * s1, 2 * s2)
x3 = np.append(2 * s2, 2 * s1)


signals = [x1, x2, x3]
times = [t1, t2, t2]
frequency = [f1, f2, f2]

for i in range(len(signals)):
    figure, axes = plt.subplots(2, constrained_layout=True)
    figure.set_size_inches(8, 6)
    y = 2 * np.abs(fft(signals[i]) / len(signals[i]))
    axes[0].plot(times[i], signals[i], linewidth=.5)
    axes[0].set_xlabel('Час, с')
    axes[0].set_ylabel("Амплітуда, В")
    axes[0].set_title("Частота")
    axes[1].stem(frequency[i], y)
    axes[1].set_xlim(0, sample_rate / 2)
    axes[1].set_xlabel('Частота, Гц')
    axes[1].set_ylabel("Амплітуда, В")
    axes[1].set_title("Спектр")
    plt.show()


