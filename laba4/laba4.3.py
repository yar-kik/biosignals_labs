"""3. Сформувати вектор відліків часу тривалістю 3 с для частоти дискретизації 128 Гц. Сформувати сигнал ділянки
синусоїди частотою 20 Гц. Створити розрив (вставити 10 нульових відліків замість відліків сигналу) в сигналі в момент
часу 1.05 с. Отримати спектр сигналу. Перемістити розрив в момент часу 2 c, розрахувати спектр. Побудувати графіки
двох сигналів з розривами та їх амплітудних спектрів. Зробити висновки щодо того, чи можливо визначити наявність та
точне розташування розриву в сигналі, аналізуючи спектр сигналу. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from numpy import sin, pi

sample_rate = 128
duration = 3
frequency = 20

time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
f = np.linspace(0, sample_rate, duration * sample_rate, endpoint=False)
x1 = sin(2 * pi * frequency * time)
x2 = sin(2 * pi * frequency * time)

breaking1 = round(1.05 * sample_rate)
breaking2 = 2 * sample_rate


x1[breaking1:breaking1 + 10] = 0
x2[breaking2:breaking2 + 10] = 0

y1 = 2 * np.abs(fft(x1) / len(x1))
y2 = 2 * np.abs(fft(x2) / len(x2))

x12 = [x1, x2]
y12 = [y1, y2]



figure, axes = plt.subplots(2, 2, constrained_layout=True)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax[0].plot(time, x12[i])
    ax[1].stem(f, y12[i])
    ax[0].set_xlabel('Час, с')
    ax[1].set_xlabel('Частота, Гц')
    # ax.set_ylabel("Амплітуда, В")
    ax[0].set_title("Частота 20 Гц")
    ax[1].set_title("Спектр")
    ax[1].set_xlim(0, sample_rate / 2)
    # ax.minorticks_on()
    # ax.grid(which='major', linewidth=1.2)
    # ax.grid(which='minor', linewidth=.5)
plt.show()