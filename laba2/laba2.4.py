import numpy as np
from laba3.services import get_signal_duration, build_multiple_plot

ekg_normal = np.load('../data/norm/1600715877.npz')
ekg_anomaly = np.load('../data/anomaly/1600717447.npz')
fs = ekg_normal['fs']
save_as = 'EKG_plot'
time_normal = get_signal_duration(ekg_normal['signal'], fs)
time_anomaly = get_signal_duration(ekg_anomaly['signal'], fs)

data_list = [
    {"title": "ЕКГ в нормі", "time": time_normal, "signal": ekg_normal['signal']},
    {"title": "ЕКГ аномальне", "time": time_anomaly, "signal": ekg_anomaly['signal']}
    ]
ylabel = ['Напруга, мВ', 'Напруга, мВ']
labels = [ekg_normal['labels'], ekg_anomaly['labels']]
labels_indexes = [ekg_normal['labels_indexes'], ekg_anomaly['labels_indexes']]

build_multiple_plot(2, data_list, title='Графіки сигналів ЕКГ', x_label='Час, с',
                    y_label=ylabel, labels=labels, labels_indexes=labels_indexes,
                    plot_name_to_save=save_as)
