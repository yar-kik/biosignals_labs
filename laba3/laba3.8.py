import numpy as np
from scipy.signal import freqz

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

sample_rate = 256
N = 100

w, h = freqz(b, a, N, fs=sample_rate)  # розрахунок КЧХ


