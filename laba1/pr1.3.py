import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt


def y(amplitude, frequency, time):
    return amplitude*sin(2*pi*frequency*time)


f = np.array([1, 10, 50])
np.random.seed(1604)
A = list(map(float, input("Введіть амплітуди синусоїд через кому:\n").split(', ')))
sample_rate = 256
t = np.arange(0, 1+1/sample_rate, 1/sample_rate)
figure, axes = plt.subplots(3)

figure.suptitle('Графіки синусоїд', fontsize=16)
figure.set_size_inches(8, 8)
for i, ax in enumerate(axes):
    ax.plot(t, y(A[i], f[i], t))
    ax.set_xlabel('Час, t')
    ax.set_ylabel('Амплітуда, A')
    ax.set_title(f'Частота {f[i]} Гц', fontsize=12)
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.show()