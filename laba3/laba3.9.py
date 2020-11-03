import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

sample_rate = 256
N = 100

w, h = freqz(b, a, N, fs=sample_rate)
frequency_response = np.abs(h)
phase_response = np.unwrap(np.angle(h))
data = [{'title': 'Амплітудно-частотна характеристика системи', 'signal': frequency_response},
        {'title': "Фазо-частотна характеристика системи", 'signal': phase_response}]
ylabel = ['Ku', "Фаза, радіани"]

figure, axes = plt.subplots(2)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax.plot(w, data[i]['signal'])
    ax.set_xlabel('Частота, Гц')
    ax.set_ylabel(ylabel[i])
    ax.set_title(data[i]['title'])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.tight_layout()
plt.show()

h_index = np.where(np.abs(h) < 1)[0]
print(f'Система послаблює сигнал на частотному діапазоні від '
      f'{round(w[h_index[0]], 2)} до {round(w[h_index[-1]], 2)} Гц')
