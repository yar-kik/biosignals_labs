import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.io import loadmat

eeg_healthy = loadmat('../data/heart_rate_norm.mat')
eeg_sick = loadmat('../data/heart_rate_apnea.mat')

eeg_healthy_data = eeg_healthy['hr_norm']/1000
eeg_sick_data = eeg_sick['hr_ap']/1000
eeg_healthy_data = eeg_healthy_data.reshape(-1, len(eeg_healthy_data))[0]
eeg_sick_data = eeg_sick_data.reshape(-1, len(eeg_sick_data))[0]

all_time_healthy = np.sum(eeg_healthy_data)
all_time_sick = np.sum(eeg_sick_data)

cum_healthy = np.cumsum(eeg_healthy_data)
cum_sick = np.cumsum(eeg_sick_data)

time_healthy = np.arange(eeg_healthy_data[0], all_time_healthy)
time_sick = np.arange(eeg_sick_data[0], all_time_sick)

interpol_healthy_signal = interp1d(x=cum_healthy, y=eeg_healthy_data)(time_healthy)
interpol_sick_signal = interp1d(x=cum_sick, y=eeg_sick_data)(time_sick)

data_list = [
    {'title': "ЕЕГ здорової людини???", 'time': time_healthy, 'cs': eeg_healthy_data, 'signal': interpol_healthy_signal, 'cum_time': cum_healthy},
    {'title': "ЕЕГ хворої людини???", 'time': time_sick, 'cs': eeg_sick_data, 'signal': interpol_sick_signal, 'cum_time': cum_sick}
    ]

figure, axes = plt.subplots(2)
figure.suptitle('Графіки сигналів', fontsize=16)
figure.set_size_inches(7, 7)
for i, ax in enumerate(axes):
    ax.plot(data_list[i]['cum_time'][2:20], data_list[i]['cs'][2:20], label='before interpol')
    ax.plot(data_list[i]['time'][2:20], data_list[i]['signal'][2:20], label='after interpol')
    ax.set_xlabel("Номер зразка")
    ax.set_ylabel('Час, с')
    ax.set_title(f'{data_list[i]["title"]}', fontsize=12)
    ax.minorticks_on()
    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linewidth=.5)
    ax.legend()
plt.tight_layout()
plt.savefig('plots/EEG_plot')
plt.show()