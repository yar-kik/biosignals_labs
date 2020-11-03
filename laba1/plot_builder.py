import matplotlib.pyplot as plt

def build_plot(x, y, title='Графік ...'):
    plt.plot(x, y, linewidth=2)
    plt.title(f'{title}', fontsize=14)
    plt.xlabel('Час, t', fontsize=10)
    plt.ylabel('Амплітуда, А', fontsize=10)
    plt.minorticks_on()
    plt.grid(which='major', linewidth=1.2)
    plt.grid(which='minor', linewidth=.5)
    plt.show()