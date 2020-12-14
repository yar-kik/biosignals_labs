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
y = np.correlate(x, x, mode="full")

plt.figure(num=1, figsize=(8, 6))
# plt.plot(t, x)
plt.stem(y)
plt.title("", fontsize=14)
plt.xlabel("", fontsize=10)
plt.ylabel("", fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()