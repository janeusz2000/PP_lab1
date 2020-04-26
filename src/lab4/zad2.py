from scipy.signal import butter, lfilter
import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep

# Global Variables
fs = 48000
max_int16 = 32767


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    range = [low, high]

    b, a = butter(order, range, btype='band')
    y = lfilter(b, a, data)
    return y


if __name__ == '__main__':
    volume_offsets = np.linspace(0, -40, num=40, endpoint=False)
    noise = fun.gen_simple(1, 0.5, 0, "noise", 0)
    ref = butter_bandpass_filter(noise, 800, 1200, fun.fs).astype(np.int16)

    offset = -6
    user_input = 'y'
    while user_input == 'y':
        left = np.copy(ref)
        left[int(fs / 4):int(3 * fs / 4)] += fun.gen_simple(0.5, 0.5, 1100, "sin", offset)
        right = np.zeros(len(left), dtype=np.int16)

        output = np.ndarray.transpose(np.array((left, right)))
        sd.play(output, fs)
        sleep(1.2)
        user_input = input("Did you hear the tone? y/n ")
        offset -= 1
    sin = fun.gen_simple(0.5, 0.5, 1100, "sin", offset)
    sin_right = np.zeros(len(sin), dtype=np.int16)
    out = np.ndarray.transpose(np.array((sin, sin_right)))
    sd.play(out, fs)
    user_input = input("Did you hear the tone? y/n ")
    print('\n' + str(offset))

