import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# sample_rate = 256
# t = np.arange(0, 10 + 1 / sample_rate, 1 / sample_rate)
# y = square(2 * np.pi * t * .5)

# U11 = np.array([26.4, 22, 18.8, 15, 11, 7.47, 3.65])/1000
# U21 = np.array([940, 819, 703, 577, 431, 287, 145])/1000
#
# U12 = np.array([26, 22.2, 18.8, 14.9, 11, 7.33, 3.6])/1000
# U22 = np.array([915, 802, 688, 565, 424, 280, 142])/1000
#
# U13 = np.array([93.1, 74.5, 56.1, 37.9, 18.7, 9.3])/1000
# U23 = np.array([45.9, 39.8, 32.4, 21.6, 3.9, 3.8])/1000

f = np.log10(np.array([20, 50, 100, 2E+2, 5E+2, 1E+3, 2E+3, 5E+3, 1E+4, 2E+4, 5E+4, 1E+5, 2E+5]))
U11 = np.array([33.4, 35.9, 36.2, 36.3, 36.3, 36.1, 36.2, 36.3, 36.0, 35, 32.6, 25.5, 15.7])
U12 = np.array([32.9, 35.2, 35.6, 35.6, 35.7, 35.7, 35.6, 35.5, 35.2, 34, 31.7, 26.1, 15.7])
U13 = np.array([3.8, 4.4, 4.6, 4.6, 4.6, 4.7, 4.6, 4.7, 5.1, 4.6, 4.6, 4.5, 4.6])

# plt.plot(f, U11, linewidth=2, label='СЕ')
# plt.plot(f, U12, linewidth=2, linestyle='--', label='СБ')
plt.plot(f, U13, linewidth=2, linestyle='-.', label='СК')
plt.legend()
# plt.scatter(U11, U21, marker='x')
plt.title('Графік частотних характеристик підсилювачів', fontsize=14)
plt.xlabel('lg f, Гц', fontsize=10)
plt.ylabel('Ku(f)', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()
