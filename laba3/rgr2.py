from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 4, -2, 7])  # поміняти значення тут
b = np.array([5, -2, -4, 7, 4])  # і тут
fs = 1000
w, h = freqz(b, a, fs=fs)

plt.plot(w, np.abs(h))
plt.title("АЧХ системи")
plt.xlabel("Частота, Гц")
plt.ylabel("Амплітуда")
plt.show()
