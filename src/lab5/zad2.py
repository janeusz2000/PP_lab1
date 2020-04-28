from scipy.signal import butter, lfilter
import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep

# Global Variables
fs = 48000
max_int16 = 32767

if __name__ == '__main__':
    sine_wav = fun.gen_simple(2, 0.5, 1000, "sin", -3, dtype=np.int32)
    sine_right = np.zeros(len(sine_wav), dtype=np.int16)
    stereo_sine = np.array([sine_wav.astype(np.int16), sine_right]).T

    h1 = fun.gen_simple(2, 0.5, 2000, "sin", -3, dtype=np.int32)
    h2 = fun.gen_simple(2, 0.5, 3000, "sin", -3, dtype=np.int32)
    h3 = fun.gen_simple(2, 0.5, 4000, "sin", -3, dtype=np.int32)

    hct = ((sine_wav + h1 + h2 + h3) / 4).astype(np.int16)
    stereo_hct = np.array([hct, sine_right]).T
    sd.play(stereo_sine, fun.fs)
    sleep(2.5)
    sd.play(hct, fun.fs)
    print(hct)
    while user_input == 'y':
        left = np.copy(ref)
        left[int(fs / 4):int(3 * fs / 4)] += fun.gen_simple(0.5, 0.2, 1000, "sin", offset)
        right = np.zeros(len(left), dtype=np.int16)

        output = np.array((left, right)).T
        sd.play(output, fs)
        sleep(1.2)
        user_input = input("Did you hear the tone? y/n ")

        offset -= 1

    input()


