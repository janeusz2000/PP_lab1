from src import functions as fun
from scipy.signal import butter, lfilter
import time
import sounddevice as sd
import numpy as np


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    range = [low, high]

    b, a = butter(order, range, btype='band')
    y = lfilter(b, a, data)
    return y


if __name__ == '__main__':
    noise_wav = fun.gen_simple(2, 0.5, 3000, "noise", -6)
    filtered_noise = butter_bandpass_filter(noise_wav, 800, 1200, fun.fs)
    noise_right = np.zeros(len(noise_wav), dtype=np.int16)
    stereo_noise = np.array([noise_wav, noise_right]).T

    user_input = ''
    sine_amp = -3

    while user_input != 'N':
        sine_wav = fun.gen_simple(0.1, 0.5, 1000, "sin", sine_amp)
        sine_right = np.zeros(len(sine_wav), dtype=np.int16)
        stereo_sine = np.array([sine_wav, sine_right]).T

        sd.play(stereo_noise, fun.fs)
        time.sleep(2)
        sd.play(stereo_sine, fun.fs)
        sine_amp -= 3
        user_input = input('Słyszysz ton? [T/N]')
    print(sine_amp + 3)
    sine_wav = fun.gen_simple(0.1, 0.5, 1000, "sin", sine_amp + 3)
    sine_right = np.zeros(len(sine_wav), dtype=np.int16)
    stereo_sine = np.array([sine_wav, sine_right]).T
    sd.play(stereo_sine, fun.fs)
    user_input = input('Słyszysz ton? [T/N]')
