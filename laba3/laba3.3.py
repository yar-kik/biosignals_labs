import numpy as np
from numpy import sin, pi
from scipy.signal import lfilter, find_peaks

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

frequency = 10
sample_rate = 256
duration = 1
amplitude = 1

time = np.linspace(0, duration, sample_rate)
x = amplitude * sin(2 * pi * frequency * time)
y = lfilter(b, a, x)

x_peaks, _ = find_peaks(np.abs(x))
y_peaks, _ = find_peaks(np.abs(y))
gain = abs(y[y_peaks[5]] / x[x_peaks[5]])

y_rad = np.arccos(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y)))
y_deg = np.rad2deg(y_rad)

print(f"Коефіцієнт підсилення передачі напруги ЛДС становить {round(gain, 2)}")
print(f"Різниця фаз між вихідним і вхідним сигналом становить {round(y_deg, 2)} градусів")
