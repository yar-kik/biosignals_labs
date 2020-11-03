import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt
from scipy.signal import lfilter


a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

frequency1 = 3
frequency2 = 20
sample_rate = 256
duration = 1
amplitude = 1

time = np.linspace(0, duration, sample_rate)
x1 = amplitude * sin(2 * pi * frequency1 * time)
x2 = amplitude * sin(2 * pi * frequency2 * time)
y1 = lfilter(b, a, x1)
y2 = lfilter(b, a, x2)


data = [{'signal_in': x1, 'signal_out': y1, 'time': time,
         'title': f'Реакція системи $y_1$ на вхідний сигнал $x_1$ (3 Гц)'},
        {"signal_in": x2, "signal_out": y2, 'time': time,
         'title': f'Реакція системи $y_2$ на вхідний сигнал $x_2$ (20 Гц)'}]
figure, axes = plt.subplots(2)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax.plot(data[i]['time'], data[i]['signal_in'], label=f'$x_{i+1}$')
    ax.plot(data[i]['time'], data[i]['signal_out'], label=f'$y_{i+1}$')
    ax.set_xlabel('Час, с')
    ax.set_ylabel("Амплітуда, В")
    ax.set_title(data[i]['title'])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
    ax.legend()
plt.tight_layout()
plt.show()

# Перевірка системи на адитивність
y_summed = lfilter(b, a, x1 + x2)
data = [{'signal': y_summed, 'time': time,
         'title': 'Реакція системи на суму двох сигналів'},
        {"signal": y1 + y2, 'time': time,
         'title': 'Сума реакцій систем на два сигнали'}]
figure, axes = plt.subplots(2)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax.plot(data[i]['time'], data[i]['signal'])
    ax.set_xlabel('Час, с')
    ax.set_ylabel("Амплітуда, В")
    ax.set_title(data[i]['title'])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.tight_layout()
plt.show()

# Перевірка системи на гомогенність
y_multiplied = lfilter(b, a, x1 * 3)
data = [{'signal': y_multiplied, 'time': time,
         'title': 'Реакція системи на сигнал з тричі більшою амплітудою'},
        {"signal": 3 * y1, 'time': time,
         'title': 'Втричі більша реакція системи на сигнал'}]
figure, axes = plt.subplots(2)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax.plot(data[i]['time'], data[i]['signal'])
    ax.set_xlabel('Час, с')
    ax.set_ylabel("Амплітуда, В")
    ax.set_title(data[i]['title'])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.tight_layout()
plt.show()
