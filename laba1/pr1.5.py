import numpy as np
import matplotlib.pyplot as plt

sample_rate = 256
t = np.arange(0, 10+1/sample_rate, 1/sample_rate)
center = np.random.random()*10
duration = float(input("Введіть тривалість імпульсу (число від 0 до 10): "))
amplitude = float(input("Введіть амплітуду: "))
start = int((center-duration/2)*sample_rate)
end = int((center+duration/2)*sample_rate)
while end >= len(t) or start <= 0:
    center = np.random.random() * 10
    end = int((center + duration / 2) * sample_rate)
    start = int((center - duration / 2) * sample_rate)

y = np.zeros_like(t)
y[start:end] = amplitude

plt.plot(t, y, linewidth=2)
plt.title('Графік прямокутного імпульсу', fontsize=14)
plt.xlabel('Час, t', fontsize=10)
plt.ylabel('Амплітуда, А', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()