from scipy.signal import butter, lfilter
import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep


if __name__ == '__main__':
    sine_wav = fun.gen_simple(2, 0.5, 1000, "sin", -20, dtype=np.int32)
    sine_right = np.zeros(len(sine_wav), dtype=np.int16)
    stereo_sine = np.array([sine_wav.astype(np.int16), sine_right]).T

    h1 = fun.gen_simple(2, 0.5, 2000, "sin", -20, dtype=np.int32)
    h2 = fun.gen_simple(2, 0.5, 3000, "sin", -20, dtype=np.int32)
    h3 = fun.gen_simple(2, 0.5, 4000, "sin", -20, dtype=np.int32)

    hct = ((sine_wav + h1 + h2 + h3) / 4).astype(np.int16)
    stereo_hct = np.array([hct, sine_right]).T
    tone_amp = -20
    user_input = ''
    while user_input != 'y':
        sine = fun.gen_simple(2, 0.5, 1000, "sin", tone_amp, dtype=np.int32)
        stereo_sine = np.array([sine_wav.astype(np.int16), sine_right]).T
        sd.play(stereo_sine, fun.fs)
        sleep(2.5)
        sd.play(stereo_hct, fun.fs)
        user_input = input("Were the sound equal in loudness? y/n ")
        tone_amp += 1
    print(tone_amp - 1)


