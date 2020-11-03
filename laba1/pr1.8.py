import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt

sample_rate = 256
t = np.arange(0, 5 + 1 / sample_rate, 1 / sample_rate)
f = float(input("Введіть частоту: "))
a = float(input("Введіть значення амплітуди: "))


def my_sin(amplitude, frequency, time):
    return amplitude * sin(2 * pi * frequency * time)


plt.figure(figsize=(10, 5))
plt.plot(t, my_sin(a, f, t), linewidth=2)
plt.title('Графік синусоїдального сигналу', fontsize=14)
plt.xlabel('Час, t', fontsize=10)
plt.ylabel('Амплітуда, А', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
