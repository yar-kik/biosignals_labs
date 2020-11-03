import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import lfilter, square

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])
sample_rate = 256
frequency = 5
duration = 1
duty = .3
time = np.linspace(0, duration, sample_rate)
x = square(2 * np.pi * time * frequency, duty)
y = lfilter(b, a, x)


plt.figure(num=1, figsize=(8, 6))
plt.plot(time, x, label='Вхідний сигнал')
plt.plot(time, y, label='Вихідний сигнал')
plt.title("Реакція системи на послідовність прямокутних імпульсів", fontsize=14)
plt.xlabel('Час, с', fontsize=10)
plt.ylabel('Амплітуда, В', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.legend(loc='upper right')
plt.show()

