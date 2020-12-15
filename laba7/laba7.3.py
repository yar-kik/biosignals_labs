"""Сформувати вектор відліків часу тривалістю 10 с для частоти
дискретизації 256 Гц. Сформувати сигнали прямокутний імпульс
амплітуди 1 В тривалості 1 сек. в момент часу 3 сек. (сигнал 1),
та прямокутного імпульсу амплітуди 1 В тривалістю 1 сек. в момент
часу 0 сек. (сигнал 2). Побудувати графік взаємнокореляційної функції,
зробити висновки щодо можливості визначення локалізації в часі
прямокутного імпульсу з використанням кореляційного аналізу."""
from typing import Union

import numpy as np
import matplotlib.pyplot as plt


def single_square(t: np.array, tau: Union[int, float]):
    """
    Функція для свторення прямокутного імпульсу
    """
    x = np.zeros(len(t))
    for k, tk in enumerate(t - tau / 2):
        if np.abs(tk) > tau/2:
            x[k] = 0
        else:
            x[k] = 1
    return x


duration = 10
sample_rate = 256
amplitude = 1
pulse_duration = 1
time_shift = 3

t = np.linspace(0, duration, duration * sample_rate)
x1 = amplitude * single_square(t, pulse_duration)
x2 = amplitude * single_square(t - time_shift, pulse_duration)
y = np.correlate(x2, x1, mode="full") / np.sum(x1 ** 2)
t_y = np.linspace(-duration, duration, len(y))

title = ["Графік сигналу 1", "Графік сигналу 2", "Графік взаємнокореляційної функції"]
x_label = ["Час, с", "Час, с", "Зсув в часі, с"]
y_label = ["Амплітуда", "Амплітуда", "Кореляція"]

figure, axes = plt.subplots(3, constrained_layout=True)
figure.set_size_inches(12, 6)
axes[0].plot(t, x1)
axes[1].plot(t, x2)
axes[2].plot(t_y, y)
for i, ax in enumerate(axes):
    ax.set_title(title[i])
    ax.set_xlabel(x_label[i])
    ax.set_ylabel(y_label[i])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.show()
