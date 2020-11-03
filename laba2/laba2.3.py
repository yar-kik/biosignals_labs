from scipy.io import loadmat

from services import get_signal_duration, build_multiple_plot

eeg_healthy = loadmat('../data/EEG_healthy/eeg_healthy_9.mat')
eeg_sick = loadmat('../data/EEG_sick/eeg_sick_9.mat')
eeg_healthy_data = eeg_healthy['sig'][0]
eeg_sick_data = eeg_sick['sig'][0]

save_as = 'EEG_plot'
sample_rate = 256
time = get_signal_duration(eeg_healthy_data, sample_rate)
data_list = [
    {'title': "ЕЕГ здорової людини", 'signal': eeg_healthy_data, 'time': time},
    {'title': "ЕЕГ хворої людини", 'signal': eeg_sick_data, 'time': time}
    ]
ylabel = ['Напруга, мкВ', 'Напруга, мкВ']
build_multiple_plot(2, data_list, title='Графіки сигналів ЕЕГ', x_label='Час, с',
                    y_label=ylabel, plot_name_to_save=save_as)
