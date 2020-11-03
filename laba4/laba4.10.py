"""10. Побудувати функцію для розрахунку та виводу на графік спектральної густини потужності сигналу, прочитаного з
файлу. В функцію передавати назву файлу з сигналом та інші необхідні дані. """

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.io import loadmat

ekg_normal = np.load('../data/norm/1600715877.npz')
ekg_anomaly = np.load('../data/anomaly/1600717447.npz')
sample_rate = ekg_normal['fs']
signal = ekg_normal['signal']
signal = ekg_anomaly['signal']

eeg_healthy = loadmat('../data/EEG_healthy/eeg_healthy_9.mat')
signal = eeg_healthy['sig'][0]
sample_rate = 256

duration = len(signal) / sample_rate

time = np.linspace(0, duration, len(signal))
frequency = np.linspace(0, sample_rate, len(signal))
y = 2 * np.abs(fft(signal) / len(signal))
power_spectral_density = y ** 2

fig, axes = plt.subplots(2, constrained_layout=True)
fig.set_size_inches(8, 6)
axes[0].plot(time, signal)
axes[1].plot(frequency, power_spectral_density)
axes[1].set_xlim(0, sample_rate / 2)
axes[0].set_xlabel('Час, с')
axes[1].set_xlabel('Частота, Гц')
# ax.set_ylabel("Амплітуда, В")
# ax[0].set_title(f"Частота {f[i]} Гц")
axes[1].set_title("Спектр")
plt.show()
