"""1. Сформувати вектор відліків часу тривалістю 5 с для частоти
дискретизації 128 Гц. Сформувати прямокутний імпульс в момент часу 3с
 тривалості 0.1 с амплітуди 1 В. Додати до сигналу випадковий шумовий
 сигнал із нульовим середнім значенням амплітуди 0.5 В. Спроектувати
 ФНЧ Батерворта для позбавлення сигналу від шуму (функції buttord,
 butter, lfilter)"""
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import buttord, butter, lfilter, freqz


def single_square(t: np.array, tau: Union[int, float]):
    """
    Функція для свторення прямокутного імпульсу
    """
    x = np.zeros(len(t))
    for k, tk in enumerate(t):
        if np.abs(tk) > tau / 2:
            x[k] = 0
        else:
            x[k] = 1
    return x


duration = 5
sample_rate = 128
t = np.arange(0, duration, 1 / sample_rate)
f = np.arange(0, sample_rate, 1 / duration)
square_amplitude = 1
square_duration = 1
noise_amplitude = .5

x_square = square_amplitude * single_square(t - square_duration, .1)
x_noise = noise_amplitude * np.random.random(len(t))
x_noise = x_noise - np.mean(x_noise)
x_mixed = x_square + x_noise

wp = 10 / (sample_rate * 0.5)  # гранична частота смуги пропускання
ws = 20 / (sample_rate * 0.5)  # гранична частота смуги затримки
gpass = 3  # максимальні втрати в смузі пропускання (дБ)
gstop = 30  # мінімальне затухання в смузі затримки (дБ)

n, wn = buttord(wp, ws, gpass, gstop)
b, a = butter(n, wn)
x_filtered = lfilter(b, a, x_mixed)


w, h = freqz(b, a, fs=sample_rate)
plt.plot(w, np.abs(h))
plt.title("Амплітудний спектр фільтру")
plt.xlabel("Частота, Гц")
plt.ylabel("Амплітуда")
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()


x = [x_square, x_noise, x_mixed, x_filtered]
title = [["Прямокутний імпульс тривалістю 0.1с", "Амплітудний спектр"],
         ['Випадковий шумовий сигнал', 'Амплітудний спектр'],
         ['Зашумлений сигнал', 'Амплітудний спектр'],
         ['Відфільтрований сигнал', 'Амплітудний спектр']]

x_label = ["Час, с", "Частота, Гц"]
figure, axes = plt.subplots(len(x), 2, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    y = 2 * np.abs(fft(x[i]) / len(x[i]))
    ax[0].plot(t, x[i])
    ax[1].stem(f, y)
    ax[1].set_xlim(0, sample_rate / 2)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()
