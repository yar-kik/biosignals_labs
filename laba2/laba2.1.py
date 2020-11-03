import numpy as np
from laba3.services import get_signal_duration, build_multiple_plot

path_standing = '../data/standing.csv'
path_running = '../data/running.csv'
path_walking = '../data/walking.csv'

paths = [path_standing, path_running, path_walking]
saves = ['standing', 'running', 'walking']

for path, save in zip(paths, saves):
    data = np.genfromtxt(path, delimiter=';', encoding='utf-8', skip_header=True)
    accelerometers = data[:, :3]
    gyroscopes = data[:, 3:]
    sample_rate = 2
    time_array = get_signal_duration(data, sample_rate)
    data_list = [
        {'title': "Акселерометр", 'signal': accelerometers, 'time': time_array},
        {'title': "Гіроскоп", 'signal': gyroscopes, 'time': time_array}
    ]
    label_y = [r'Прискорення, $\frac{м}{с^{2}}$',
               r'Кутова швидкість, $\frac{град.}{с}$']
    legend = ["X", 'Y', 'Z']
    build_multiple_plot(2, data_list, title=f'Графіки сигналів ({save})',
                        x_label='Час, с', y_label=label_y, legend=legend,
                        plot_name_to_save=save)
