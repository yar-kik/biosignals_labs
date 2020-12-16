import numpy as np
import matplotlib.pyplot as plt
import pywt

a = [np.arange(.2, 1, .2), np.arange(2, 22, 2)]
a = np.hstack(a)
sample_rate = 128
duration = 3
frequency = 20

time = np.linspace(0, duration, duration * sample_rate, endpoint=False)
x1 = np.sin(2 * np.pi * frequency * time)
x2 = np.copy(x1)
breaking1 = round(1.05 * sample_rate)
breaking2 = 2 * sample_rate

x1[breaking1:breaking1 + 10] = 0
x2[breaking2:breaking2 + 10] = 0
x = [x1, x2]

x_label = ["Час, с", "Час, с"]
y_label = ["Амплітуда", "Масштаб"]
title = [['Сигнал із розривом в момент часу 1.05с', "Скейлограма"],
         ["Сигнал із розривом в момент часу 2.0с", "Скейлограма"]]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    cwt_matrix, _ = pywt.cwt(x[i], a, "gaus1")
    ax[0].plot(time, x[i])
    im = ax[1].imshow(abs(cwt_matrix), cmap='hot', aspect='auto', extent=[time[0], time[-1], a[-1], a[0]])
    cbar = figure.colorbar(im, ax=ax[1])
    ax[1].invert_yaxis()
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel(y_label[j])
plt.show()

