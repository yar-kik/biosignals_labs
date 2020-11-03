import numpy as np

from laba3.services import build_single_plot

path_to_data = '../data/cop_data/data/acrobats/base_open/9.csv'
path_to_data = '../data/cop_data/data/acrobats/sway_front-back_60/8.csv'

data = np.genfromtxt(path_to_data)

signal_weight = data[:, 1:5]
time = data[:, 0] - data[:, 0][0]
legend_weight = ['top left', 'top right', 'bottom left', 'bottom right']
signal_x = data[:, 5]
signal_y = data[:, 6]

build_single_plot(time, signal_weight, title='Графік стабілограми (вага)', x_label='Час, с',
                  y_label='Кілограм-сила, кгс', legend=legend_weight, plot_name_to_save='weight_plot')
build_single_plot(signal_x, signal_y, title='Графік стабілограми (координати)',
                  x_label='Вісь X, см', y_label='Вісь Y, см', plot_name_to_save='coord_plot')
