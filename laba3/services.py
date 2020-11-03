from typing import List, Union, Tuple

import numpy as np
import matplotlib.pyplot as plt


def get_signal_duration(data: np.array, sample_rate: float) -> np.array:
    """Створює масив з відліками часу"""
    samples = len(data)
    end_time = samples / sample_rate
    time_array = np.linspace(0, end_time, samples)
    return time_array


def build_multiple_plot(num_of_plots: int, data: List[dict], *, title: str = None,
                        x_label: str = None, y_label: list = None, legend: Union[list, str] = None,
                        plot_name_to_save: str = None, labels: list = None, labels_indexes: list = None,
                        color: str = None) -> None:
    """Функція для побудови кількох графіків на одному полі за списком даних"""
    figure, axes = plt.subplots(num_of_plots)
    figure.suptitle(title, fontsize=16)
    figure.set_size_inches(8, 6)
    for i, ax in enumerate(axes):
        handles = ax.plot(data[i]['time'], data[i]['signal'], c=color)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label[i])
        ax.set_title(f'{data[i]["title"]}', fontsize=12)
        ax.minorticks_on()
        ax.grid(which='major', linewidth=1.2)
        ax.grid(which='minor', linewidth=.5)
        if legend:
            ax.legend(handles, legend)
        if labels:
            for label, labels_index in zip(labels[i], labels_indexes[i]):
                ax.text(s=label, x=data[i]['time'][labels_index], y=data[i]['signal'][labels_index])
    plt.tight_layout()
    if plot_name_to_save:
        plt.savefig(f"{plot_name_to_save}.png")
    plt.show()


def build_single_plot(x: np.array, y: np.array, *,
                      size: Tuple[int, int] = (7, 7),
                      x_label: str = None, y_label: str = None, legend: Union[list, str] = None,
                      title: str = None, plot_name_to_save: str = None) -> None:
    """Функція побудови одиничного графіка за даними"""
    plt.figure(num=1, figsize=size)
    handles = plt.plot(x, y)
    plt.title(title, fontsize=14)
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.minorticks_on()
    plt.grid(which='major', linewidth=1.2)
    plt.grid(which='minor', linewidth=.5)
    if legend:
        plt.legend(handles, legend)
    if plot_name_to_save:
        plt.savefig(f"{plot_name_to_save}.png")
    plt.show()



