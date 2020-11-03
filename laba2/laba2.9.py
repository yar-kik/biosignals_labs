import numpy as np
from laba3.services import build_single_plot, get_signal_duration
from scipy.io import loadmat

a = np.arange(0, 10)
b = np.arange(20, 30)
# c = np.vstack((a, b)).T
# c = np.array((a, b)).T
c = np.column_stack((a, b))


def build_plot_by_signal_section(start: float, end: float, signal: np.array, fs: int) -> np.ndarray:
    """Функція побудови графіку за заданим інтервалом часу, масивом даних та частотою дискретизації.
    На виході функції вектор з відліками часу і сигналу"""
    time = get_signal_duration(signal, fs)
    start_id = int(start * fs)
    end_id = int(end * fs) + 1
    if start_id < 0 or end_id > len(time) or start_id > end_id:
        return f"Введено некоректний проміжок. Проміжок має бути від 0 до {round(len(time)/fs, 2)} секунд"
    section_time = time[start_id:end_id]
    section_signal = signal[start_id:end_id]
    build_single_plot(section_time, section_signal)
    return np.column_stack((section_time, section_signal))


eeg_healthy = loadmat('../data/EEG_healthy/eeg_healthy_9.mat')
eeg_healthy_data = eeg_healthy['sig'][0]

print(build_plot_by_signal_section(2, 5, eeg_healthy_data, 256))