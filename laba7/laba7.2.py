"""2. Сформувати вектор відліків часу тривалістю 1 с для частоти
дискретизації 256 Гц. Сформувати дискретний аналог сигналу
x(t) = 5cos(2pi * 50t) + 2cos(2pi * 100t).
Побудувати графік автокореляційної функції. Зробити висновки щодо
характеру АКФ для періодичного сигналу."""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, cos

duration = 1
sample_rate = 256
t = np.linspace(0, duration, duration * sample_rate)
x = 5 * cos(2 * pi * 50 * t) + 2 * cos(2 * pi * 100 * t)
y = np.correlate(x, x, mode="full") / np.sum(x ** 2)
t_y = np.linspace(-duration, duration, len(y))

title = ["Графік сигналу", "Графік автокореляційної функції"]
x_label = ["Час, с", "Зсув в часі, с"]
y_label = ["Амплітуда", "Автокореляція"]

figure, axes = plt.subplots(2, constrained_layout=True)
figure.set_size_inches(12, 6)
axes[0].plot(t, x)
axes[1].stem(t_y, y)
for i, ax in enumerate(axes):
    ax.set_title(title[i])
    ax.set_xlabel(x_label[i])
    ax.set_ylabel(y_label[i])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.show()
