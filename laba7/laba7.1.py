"""1. Сформувати вектор відліків часу тривалістю 1 с для частоти
дискретизації 256 Гц. Сформувати сигнал випадкового білого гаусівського
шуму (функція randn). Розрахувати та побудувати графік автокореляційної
функції. Зробити висновки щодо характеру АКФ для шума."""

import numpy as np
import matplotlib.pyplot as plt

duration = 1
sample_rate = 256
t = np.linspace(0, duration, duration * sample_rate)
x = np.random.randn(len(t))
y = np.correlate(x, x, mode="full") / sum(x ** 2)  # нормування значень

title = ["Графік сигналу із нормальним розподілом",
         "Графік автокореляційної функції"]
x_label = ["Час, с", "Лаг"]
y_label = ["Амплітуда", "Автокореляція"]
figure, axes = plt.subplots(2, constrained_layout=True)
figure.set_size_inches(12, 6)
axes[0].plot(t, x)
axes[1].stem(y)
for i, ax in enumerate(axes):
    ax.set_title(title[i])
    ax.set_xlabel(x_label[i])
    ax.set_ylabel(y_label[i])
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
plt.show()
