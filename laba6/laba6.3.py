"""3. Сформувати вектор відліків часу тривалістю 10 с для частоти
дискретизації 128 Гц. Сформувати випадковий сигнал амплітуди 10 мВ
з нульовим середнім значенням, який зашумлений мережевою перешкодою
частоти 50 Гц амплітуди 1 В. Спроектувати ЗФ Батерворта для позбавлення
сигналу від перешкоди."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import buttord, butter, lfilter, freqz


duration = 10
sample_rate = 128
frequency = 50
t = np.arange(0, duration, 1 / sample_rate)
f = np.arange(0, sample_rate, 1 / duration)
net_noise_amplitude = 1
random_amplitude = 0.01

x_net_noise = net_noise_amplitude * np.sin(2 * np.pi * frequency * t)
x_random = 2 * random_amplitude * np.random.random(len(t))
x_random = x_random - np.mean(x_random)
x_mixed = x_random + x_net_noise

wp = [40 / (sample_rate * 0.5), 60 / (sample_rate * 0.5)]
ws = [49 / (sample_rate * 0.5), 51 / (sample_rate * 0.5)]
gpass = 3
gstop = 60

n, wn = buttord(wp, ws, gpass, gstop)
b, a = butter(n, wn, btype='bandstop')
x_filtered = lfilter(b, a, x_mixed)

w, h = freqz(b, a, fs=sample_rate)
plt.plot(w, np.abs(h))
plt.title("Амплітудний спектр ЗФ")
plt.xlabel("Частота, Гц")
plt.ylabel("Амплітуда")
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()


x = [x_random, x_net_noise, x_mixed, x_filtered]
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
    if i == 3:
        ax[0].set_ylim(-.01, .01)
    for j in range(2):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()
