import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, TransferFunction, dimpulse

a = np.array([1, 7/140, -6/130, 0, -1/150, 1/150])
b = np.array([0, -6/20, -4/20, 0, 6/20, -4/20])

samples = 30
x = TransferFunction(b, a, dt=True)
signal_in = dimpulse(x, n=samples)

plt.figure(num=1, figsize=(8, 6))
plt.stem(signal_in[0], signal_in[1][0])
plt.title("Графік вихідного сигналу", fontsize=14)
plt.xlabel('Номер відліку', fontsize=10)
plt.ylabel('Амплітуда, В', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()

