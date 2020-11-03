from scipy.signal import freqz
import numpy as np
from services import build_single_plot


a = np.array([1, 4, -2, 7])
b = np.array([5, -2, -4, 7, 4])
fs = 1000
w, h = freqz(b, a, fs=fs)
h_index = np.where(np.abs(h) > 1)[0]
print(f'Система підсилює сигнал на частотному діапазоні від {round(w[h_index[0]], 2)} до {round(w[h_index[-1]], 2)} Гц')
build_single_plot(w, np.abs(h), size=(8, 6), title='Амплітудно-частотна характеристика системи',
                  x_label='Частота, Гц', y_label='Амплітуда')
