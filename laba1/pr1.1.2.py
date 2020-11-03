import numpy as np
import matplotlib.pyplot as plt

random_range = np.random.randn(1000)

plt.hist(random_range, 100)
plt.title('Гістограми випадкових чисел з нормальним розподілом', fontsize=14)
plt.xlabel('Ймовірність, P', fontsize=10)
plt.ylabel('Кількість чисел, N', fontsize=10)
plt.minorticks_on()
plt.grid(which='major', linewidth=1.2)
plt.grid(which='minor', linewidth=.5)
plt.show()