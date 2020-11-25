"""2. Сформувати вектор відліків часу тривалістю 1 с для частоти
дискретизації 128 Гц. Сформувати сигнали ділянки синусоїди частотою
10 Гц амплітуди 1 В. Додати випадковий сигнал з нульовим середнім
значенням амплітуди 2 В. Спроектувати ФНЧ, ФВЧ та СФ Чебишова І роду
для позбавлення сигналу від шуму (cheb1ord, cheby1)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import cheb1ord, cheby1, lfilter, freqz

duration = 1
sample_rate = 128
frequency = 10
t = np.arange(0, duration, 1 / sample_rate)
f = np.arange(0, sample_rate, 1 / duration)
sin_amplitude = 1
noise_amplitude = 2

x_sin = sin_amplitude * np.sin(2 * np.pi * frequency * t)
x_noise = 2 * noise_amplitude * np.random.random(len(t))
x_noise = x_noise - np.mean(x_noise)
x_mixed = x_sin + x_noise


x = [x_sin, x_noise, x_mixed]
title = [["Синусоїда з частотою 10Гц", "Амплітудний спектр"],
         ['Шум', 'Амплітудний спектр'],
         ['Зашумлений сигнал', 'Амплітудний спектр']]
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

wp = [11 / (sample_rate * 0.5), 9 / (sample_rate * 0.5),
      [9 / (sample_rate * 0.5), 11 / (sample_rate * 0.5)]]  # гранична частота смуги пропускання
ws = [14 / (sample_rate * 0.5), 7 / (sample_rate * 0.5),
      [8 / (sample_rate * 0.5), 11.4 / (sample_rate * 0.5)]]  # гранична частота смуги затримки
gpass = 3  # максимальні втрати в смузі пропускання (дБ)
gstop = 30  # мінімальне затухання в смузі затримки (дБ)

x_label = ["Частота, Гц", "Час, с", "Частота, Гц"]
type = ['lowpass', 'highpass', 'bandpass']
title = [["Амплітудний спектр ФНЧ", 'Сигнал після використання ФНЧ', 'Амплітудний спектр'],
         ["Амплітудний спектр ФВЧ", "Сигнал після використання ФВЧ", "Амплітудний спектр"],
         ["Амплітудний спектр СФ", "Сигнал після використання СФ", "Амплітудний спектр"]]
figure, axes = plt.subplots(3, 3, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    n, wn = cheb1ord(wp[i], ws[i], gpass, gstop)
    b, a = cheby1(n, .5, wn, btype=type[i])
    x_filtered = lfilter(b, a, x_mixed)
    w, h = freqz(b, a, fs=sample_rate)
    y = 2 * np.abs(fft(x_filtered) / len(x_filtered))

    ax[0].plot(w, np.abs(h))
    ax[1].plot(t, x_filtered)
    ax[2].stem(f, y)
    ax[2].set_xlim(0, sample_rate / 2)
    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()