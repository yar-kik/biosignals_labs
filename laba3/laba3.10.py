from typing import Tuple
import numpy as np
from scipy.signal import freqz


def system_response(frequency, sample_rate: int = 256, n: int = 100) -> Tuple[np.array, np.array]:
    """Функція визначення АЧХ та ФЧХ системи для довільної частоти """
    a = np.array([1, 7 / 140, -6 / 130, 0, -1 / 150, 1 / 150])
    b = np.array([0, -6 / 20, -4 / 20, 0, 6 / 20, -4 / 20])
    w, h = freqz(b, a, n, fs=sample_rate)
    k = np.argmin(abs(w - frequency))
    frequency_response = np.abs(h[k])
    phase_response = np.unwrap(np.angle([h[k]]))[0]
    return frequency_response, phase_response


f, ph = system_response(10)
print(f'Значання коефіцієнта підсилення становить {round(f, 2)}, '
      f'а значення зсуву фаз становить {round(ph, 2)} радіан')