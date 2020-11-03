import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth, gausspulse

sample_rate = 256
t = np.arange(0, 10 + 1 / sample_rate, 1 / sample_rate)
triangle_signal = sawtooth(2 * np.pi * t)
square_signal = square(2 * np.pi * t)
gauss_signal = gausspulse(t-5, fc=3)
impulses = [triangle_signal, square_signal, gauss_signal]
impulses_name = ["Трикутний імпульс", "Прямокутний імпульс", "Гаусівський імпульс"]

figure, axes = plt.subplots(3)
figure.suptitle('Графіки імпульсів', fontsize=16)
for i, ax in enumerate(axes):
    ax.plot(t, impulses[i])
    ax.set_xlabel('Час, t')
    ax.set_ylabel('Амплітуда, A')
    ax.set_title(f'{impulses_name[i]}', fontsize=12)
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.show()

# plt.plot(t, gauss_signal, linewidth=2)
# plt.title('Графік послідовних прямокутних імпульсів', fontsize=14)
# plt.xlabel('Час, t', fontsize=10)
# plt.ylabel('Амплітуда, А', fontsize=10)
# plt.minorticks_on()
# plt.grid(which='major', linewidth=1.2)
# plt.grid(which='minor', linewidth=.5)
# plt.show()
