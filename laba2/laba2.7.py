import numpy as np
from laba3.services import build_multiple_plot


def mean_by_interval(data, interval):
    """Обраховує середнє значення заданих інтервалів масиву"""
    array_len = len(data)
    end = array_len - array_len % interval
    if array_len % interval:
        mean = np.append(np.mean(data[:end].reshape(-1, interval), axis=1), np.mean(data[end:]))
    else:
        mean = np.array([np.mean(i) for i in np.array_split(data, array_len / interval)])
    return mean


data = np.genfromtxt('../data/signals/Subject9_SpO2Hr.csv', delimiter=',', skip_header=True)
heart_rate = data[:, 3]
spo2 = data[:, 2]
time = data[:, 1]
interval = 30
mean_hr = mean_by_interval(heart_rate, interval)
mean_time = mean_by_interval(time, interval)
mean_spo2 = mean_by_interval(spo2, interval)

data_list = [
    {"title": "Сатурація артеріальної крові киснем", "time": time, "signal": spo2},
    {"title": "Серцевий ритм", "time": time, "signal": heart_rate}
    ]

data_list_mean = [{'title': "Середнє значення сатурації", 'signal': mean_spo2, 'time': mean_time},
                  {'title': "Середнє значення серцевого ритму", 'signal': mean_hr, 'time': mean_time}]
y_label = [r"$SpO_2$", "ударів/хв"]

build_multiple_plot(2, data_list, title='Графік сигналів серцевого ритму та сатурації',
                    x_label="Час, с", y_label=y_label, color='blue', plot_name_to_save='hr_spo2')
build_multiple_plot(2, data_list_mean, title='Графік сигналів серцевого ритму та сатурації (середні значення)',
                    x_label="Час, с", y_label=y_label, color='red', plot_name_to_save='hr_spo2_mean')
