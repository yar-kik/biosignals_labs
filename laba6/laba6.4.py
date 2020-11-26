"""4. Для звукових сигналів, які отримані з різною частотою дискретизації,
виконати допомогою фільтрів розділення на три спектральні діапазони:
до 450 Гц; від 450 Гц до 1 кГц; від 1 кГц до 4 кГц. Прослухати отримані
сигнали, зробити висновки."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import buttord, butter, lfilter, freqz

import sounddevice as sd
import soundfile as sf


audio1 = '../data/record_8000Hz.wav'

signal1, sample_rate1 = sf.read(audio1, dtype='float32')

t1 = np.linspace(0, len(signal1) / sample_rate1, len(signal1), endpoint=False)
f1 = np.linspace(0, sample_rate1, len(signal1))

wp = [350 / (sample_rate1 * 0.5),
      [450 / (sample_rate1 * 0.5), 1000 / (sample_rate1 * 0.5)],
      1000 / (sample_rate1 * 0.5)]
ws = [450 / (sample_rate1 * 0.5),
      [350 / (sample_rate1 * 0.5), 1100 / (sample_rate1 * 0.5)],
      900 / (sample_rate1 * 0.5)]
gpass = 3
gstop = 20

title = ['Графік аудіофайлу частоти 8000Гц', 'Амплітудний спектр']
x_label = ['Час, с', 'Частота, Гц']
figure, ax = plt.subplots(2, constrained_layout=True)
figure.set_size_inches(8, 6)
# відтворення записаного файлу
sd.play(signal1, sample_rate1)
sd.wait()

y = 2 * np.abs(fft(signal1) / len(signal1))
ax[1].plot(t1, signal1)
ax[0].stem(f1, y)
ax[0].set_xlim(0, sample_rate1 / 2)
for j in range(2):
    ax[j].set_xlabel(x_label[j])
    ax[j].set_title(title[j])
    ax[j].set_ylabel("Амплітуда")
    ax[j].minorticks_on()
    ax[j].grid(which='major', linewidth=1.2)
    ax[j].grid(which='minor', linewidth=.5)
plt.show()

title = [["Фільтр в частотному діапазоні до 450Гц", "Відфільтрований сигнал", "Амплітудний спектр"],
         ["Фільтр в частотному діапазоні від 450Гц до 1кГц", 'Відфільтрований сигнал', 'Амплітудний спектр'],
         ["Фільтр в частотному діапазоні від 1кГц до 4кГц", 'Відфільтрований сигнал', 'Амплітудний спектр']]

type = ['lowpass', 'bandpass', 'highpass']
x_label = ["Частота, Гц", "Час, с", "Частота, Гц"]
figure, axes = plt.subplots(len(wp), 3, constrained_layout=True)
figure.set_size_inches(12, 6)
for i, ax in enumerate(axes):
    n, wn = buttord(wp[i], ws[i], gpass, gstop)
    b, a = butter(n, wn, btype=type[i])
    x_filtered = lfilter(b, a, signal1)
    # відтворення відфільтрованого файлу
    sd.play(x_filtered, sample_rate1)
    sd.wait()

    w, h = freqz(b, a, fs=sample_rate1)
    y = 2 * np.abs(fft(x_filtered) / len(x_filtered))
    ax[0].plot(w, np.abs(h))
    ax[1].plot(t1, x_filtered)
    ax[2].stem(f1, y)
    ax[2].set_xlim(0, sample_rate1 / 2)
    for j in range(3):
        ax[j].set_xlabel(x_label[j])
        ax[j].set_title(title[i][j])
        ax[j].set_ylabel("Амплітуда")
        ax[j].minorticks_on()
        ax[j].grid(which='major', linewidth=1.2)
        ax[j].grid(which='minor', linewidth=.5)
plt.show()
