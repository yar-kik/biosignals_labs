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
    for k, tk in enumerate(t):
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
y = np.correlate(x1, x2, mode="same")

plt.figure(num=1, figsize=(8, 6))
# plt.plot(t, x1, t, x2)
plt.plot(t, y)
plt.title("", fontsize=14)
plt.xlabel("", fontsize=10)
plt.ylabel("", fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()