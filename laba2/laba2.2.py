import sounddevice as sd
import soundfile as sf
from laba3.services import build_single_plot, get_signal_duration
import datetime
from scipy.io.wavfile import write
import os


def record_sound(duration: float, fs: int = 44100, path: str = '') -> str:
    """Функція запису аудіофайлу з виведенням назви файлу. Приймає параметри:
    тривалість запису (в секундах); частота дискретизації; шлях, куди створити файл
    (за замовчуванням - поточна директорія)"""
    if not os.path.exists(path):
        os.mkdir(path)
    frames = int(fs * duration)
    filename = f'{path}record_{fs}_{datetime.datetime.now().strftime("%H%M%S")}.wav'
    print('Йде запис...')
    record = sd.rec(frames=frames, samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, record)
    print('Запис завершено!')
    return filename


sample_rate = 8000  # при записі іншого аудіфайлу замінюється значення дискретизації на 44100

duration = 5
path_to_save = '../data/sound_records/'
# запис аудіофайлу
filename = record_sound(duration, sample_rate, path_to_save)
data, _ = sf.read(filename, dtype='float32')
time = get_signal_duration(data, sample_rate)
# побудова графіку
build_single_plot(time, data, x_label='Час, t', y_label='Амплітуда, А', size=(12, 4),
                  title=f'Графік аудіофайлу {sample_rate}Гц', plot_name_to_save=f'sound_plot_{sample_rate}')

# відтворення записаного файлу
sd.play(data, sample_rate)
sd.wait()
