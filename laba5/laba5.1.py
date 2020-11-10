"""1. За допомогою функції windows ознайомитися з часовими характеристиками
та спектрами всіх вагових віконних функцій. Згідно варіантів, вказаних
в таблиці 1 (за списком, відрахувати свій номер і взяти два рядки з таблиці;
після останнього номеру починати рахувати спочатку),
сформувати вікна заданого типу та тривалості 256 відліків (функція get_window).
Побудувати графіки вікон та їх амплітудних спектрів."""
import numpy as np
from scipy.signal.windows import get_window
from scipy.fft import fft
import matplotlib.pyplot as plt


N = 256

x1 = get_window("flattop", N)
x2 = get_window("hamming", N)
y1 = 2 * np.abs(fft(x1) / len(x1))
y2 = 2 * np.abs(fft(x2) / len(x2))
x = [x1, x2]
y = [y1, y2]

fig, axes = plt.subplots(2, 2, constrained_layout=True)
for i, ax in enumerate(axes):
    ax[0].plot(x[i])
    ax[1].stem(y[i])
    for a in ax:
        a.minorticks_on()
        a.grid(which='major', linewidth=1.2)
        a.grid(which='minor', linewidth=.5)
plt.show()
