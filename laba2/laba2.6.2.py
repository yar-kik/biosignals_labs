import numpy as np


def statistic_param(data: np.ndarray, file_name: str) -> np.ndarray:
    header = 'Середнє значення;Медіанне значення;Середньоквадратичне відхилення;Дисперсія'
    empty = np.empty((0, 4))
    for signal in data:
        mean = np.mean(signal)
        median = np.median(signal)
        std = np.std(signal)
        variance = np.var(signal)
        statistic = np.array([[mean, median, std, variance]])
        empty = np.append(empty, statistic, axis=0)
    np.savetxt(f'{file_name}.csv', empty, delimiter=';', header=header)
    return empty


handball_close = '../data/cop_data/data/handball/base_close/9.csv'
acrobats_close = '../data/cop_data/data/acrobats/base_close/9.csv'
handball_front_back_60 = '../data/cop_data/data/handball/sway_front-back_60/9.csv'
acrobats_front_back_60 = '../data/cop_data/data/acrobats/sway_front-back_60/8.csv'

data_hc = np.genfromtxt(handball_close)
data_ac = np.genfromtxt(acrobats_close)
data_hfb60 = np.genfromtxt(handball_front_back_60)
data_afb60 = np.genfromtxt(acrobats_front_back_60)

data_weight = [data_hc[:, 1:-3], data_hfb60[:, 1:-3], data_ac[:, 1:-3], data_afb60[:, 1:-3]]
data_coor = [data_hc[:, -3:-1], data_hfb60[:, -3:-1], data_ac[:, -3:-1], data_afb60[:, -3:-1]]





