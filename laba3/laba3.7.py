"""7. Розрахувати реакцію системи на сигнал з п. 2.1 з
використанням функції розрахунку згортки convolve. Побудувати
графіки вхідного та вихідного сигналу, аналогічні п. 2.1
(з нульовими початковими умовами). Всі отримані в п. 7 результати
порівняти з п 2.1. Зробити висновки."""
import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt
from scipy.signal import lfilter, TransferFunction, convolve, unit_impulse

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

frequency = 10
sample_rate = 256
duration = 1
amplitude = 1

time1 = np.linspace(0, duration, sample_rate)
signal_in = amplitude * sin(2 * pi * frequency * time1)
x = unit_impulse(len(a) + len(b))
y = lfilter(b, a, x)

signal_out = convolve(y, signal_in)
time2 = np.linspace(0, len(signal_out) / sample_rate, len(signal_out))

plt.figure(num=1, figsize=(8, 6))
plt.plot(time1, signal_in, label='Вхідний сигнал', linewidth=1)
plt.scatter(time1, signal_in, marker='.', s=20)
plt.plot(time2, signal_out, label='Вихідний сигнал', linewidth=1)
plt.scatter(time2, signal_out, marker='.', s=20)
plt.xlabel("Час, с", fontsize=10)
plt.ylabel('Амплітуда, B', fontsize=10)
plt.title("Графіки сигналів", fontsize=14)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.legend()
plt.show()
