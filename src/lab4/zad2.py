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
    volume_offsets = np.linspace(0, -12, num=20, endpoint=False)
    ref = butter_bandpass_filter(fun.gen_simple(1, 0.3, 0, "noise", 0), 800, 1200, fs)

    choices = []
    tests = []
    for offset in volume_offsets:
        left = np.copy(ref)
        left[int(fs / 4):int(3 * fs / 4)] += fun.gen_simple(0.5, 0.3, 1100, "sin", offset)
        right = np.zeros((np.size(left))).astype(np.int16)

        output = np.ndarray.transpose(np.array((left, right)))
        sd.play(output, fs)
        sleep(1.2)
        choice = input("Did you hear the tone? y/n ")
        choices.append(choice)
        tests.append(offset)

    with open("../../output/lab4/zad2_results.txt", "w") as f:
        for (test, choice) in zip(tests, choices):
            f.write(f'Różnica {test}, wcisnieto {choice}\n')
