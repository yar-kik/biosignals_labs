import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, unit_impulse

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

samples = 30
signal_in = unit_impulse(samples, 1)
signal_out = lfilter(b, a, signal_in)
data = [{"title": "Вхідний сигнал (одиничний імпульс)", "signal": signal_in},
        {"title": "Вихідний сигнал (імпульсна характеристика)", "signal": signal_out}]

figure, axes = plt.subplots(2)
figure.set_size_inches(8, 6)
for i, ax in enumerate(axes):
    ax.stem(data[i]['signal'])
    ax.set_xlabel('Номер віділку')
    ax.set_ylabel("Амплітуда, В")
    ax.set_title(data[i]['title'])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.tight_layout()
plt.show()
