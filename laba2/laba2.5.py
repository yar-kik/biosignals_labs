import numpy as np
from scipy.interpolate import interp1d
from scipy.io import loadmat
from services import build_multiple_plot

# завантаження даних із матфайлу
eeg_healthy = loadmat('../data/heart_rate_norm.mat')
eeg_sick = loadmat('../data/heart_rate_apnea.mat')
# отримання значень сигналу, приведення до нормального виду та переведення значень в секунди
eeg_healthy_data = eeg_healthy['hr_norm'].T[0]/1000
eeg_sick_data = eeg_sick['hr_ap'].T[0]/1000
# отримання загального часу
all_time_healthy = np.sum(eeg_healthy_data)
all_time_sick = np.sum(eeg_sick_data)
print(f"Загальний час кардіоритмограми (норма): {round(all_time_healthy/3600, 2)} год.")
print(f"Загальний час кардіоритмограми (хвороба): {round(all_time_sick/3600, 2)} год.")
# отримання "комулятивного" масиву часу
cumulative_time_healthy = np.cumsum(eeg_healthy_data)
cumulative_time_sick = np.cumsum(eeg_sick_data)
# формування нормованого часу з дискертизацієї 1Гц
time_healthy = np.arange(eeg_healthy_data[0], all_time_healthy)
time_sick = np.arange(eeg_sick_data[0], all_time_sick)
# інтерполяція сигналу на основі комулятивного часу та старих даних. Отримання нових даних з дискретизацією 1Гц
interpol_healthy_signal = interp1d(x=cumulative_time_healthy, y=eeg_healthy_data)(time_healthy)
interpol_sick_signal = interp1d(x=cumulative_time_sick, y=eeg_sick_data)(time_sick)

data_list_old = [
    {'title': "КРГ здорової людини", 'time': cumulative_time_healthy, 'signal': eeg_healthy_data},
    {'title': "КРГ хворої людини", 'time': cumulative_time_sick, 'signal': eeg_sick_data}
]

data_list_new = [
    {'title': "КРГ здорової людини", 'signal': interpol_healthy_signal[2:100], 'time': time_healthy[2:100]},
    {'title': "КРГ хворої людини", 'signal': interpol_sick_signal[2:100], 'time': time_sick[2:100]}
]
ylabel = ['Час, с', 'Час, с']

build_multiple_plot(2, data_list_old, title='Графіки сигналів КРГ до інтерполяції',
                    x_label='Час, с', y_label=ylabel, plot_name_to_save='KRG_old', color='blue')
build_multiple_plot(2, data_list_new, title='Графіки сигналів КРГ після інтерполяції',
                    x_label="'Час, с'", y_label=ylabel, plot_name_to_save='KRG_new', color='red')
