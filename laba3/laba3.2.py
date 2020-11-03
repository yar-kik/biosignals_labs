import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt
from scipy.signal import lfilter


a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

frequency = 10
sample_rate = 256
duration = 1
amplitude = 1

zi = np.random.rand(max(len(a), len(b)) - 1)

time = np.linspace(0, duration, sample_rate)
signal_sin = amplitude * sin(2 * pi * frequency * time)

y = lfilter(b, a, signal_sin)
y2 = lfilter(b, a, signal_sin, zi=zi)[0]

t_end = np.where(time <= .1)[0][-1]
data = [[time, signal_sin, y, y2],
        [time[:t_end], signal_sin[:t_end], y[:t_end], y2[:t_end]]]

for i in data:
    plt.figure(num=1, figsize=(8, 6))
    plt.plot(i[0], i[1], label='Вхідний сигнал', linewidth=1)
    plt.scatter(i[0], i[1], marker='.', s=20)
    plt.plot(i[0], i[2], label='Вихідний сигнал (нульові початкові умови)', linewidth=1)
    plt.scatter(i[0], i[2], marker='.', s=20)
    plt.plot(i[0], i[3], label='Вихідний сигнал (випадковий початкові умови)', linewidth=1)
    plt.scatter(i[0], i[3], marker='.', s=20)
    plt.title('', fontsize=14)
    plt.xlabel("Час, с", fontsize=10)
    plt.ylabel('Амплітуда, B', fontsize=10)
    plt.minorticks_on()
    plt.grid(which='major', linewidth=1.2)
    plt.grid(which='minor', linewidth=.5)
    plt.legend()
    plt.show()