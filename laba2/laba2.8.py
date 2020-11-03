import numpy as np
from laba3.services import get_signal_duration, build_single_plot

signal = np.load('../data/TBI_ICP.npy')

sample_rate = 125
time = get_signal_duration(signal, sample_rate)

build_single_plot(time, signal, x_label="Час, с", y_label="Тиск, мм рт.ст.",
                  title="Графік внутрішньочерепного тиску",
                  plot_name_to_save="intracranial_pressure_plot")