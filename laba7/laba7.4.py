"""4. Повторити п. 3, попередньо додавши до сигналу 1 шум
з нульовим середнім значенням. Зробити висновки, порівняти з п. 3."""

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
noise = np.random.random(duration * sample_rate)
noise = noise - np.mean(noise)

x1 = x1 + noise
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