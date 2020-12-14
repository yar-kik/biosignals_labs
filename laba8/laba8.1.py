"""1. Побудувати графіки 256 відліків вейвлету Рікера та вейвлету Морле."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ricker, morlet2

points = 256
width = 4
wavelet_ricker = ricker(points, width)
wavelet_morlet = np.abs(morlet2(points, width))
wavelets = [wavelet_ricker, wavelet_morlet]
figure, axes = plt.subplots(2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    ax.plot(wavelets[i])
    for j in range(len(wavelets)):
        ax.set_xlabel("Номер відліку")
        ax.set_title("")
        ax.set_ylabel("Амплітуда")
        ax.minorticks_on()
        ax.grid(which='major', linewidth=1.2)
        ax.grid(which='minor', linewidth=.5)
plt.show()
