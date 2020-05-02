import numpy as np
import sounddevice as sd
from time import sleep
import src.functions as fun

# Global Variables
fs = 48000
max_int16 = 32767


def hct(freq_b, duration, fs, which_turned_off=[False, False, False, False]):
    output = np.zeros(duration*fs)
    if not which_turned_off[0]:
        output += fun.gen_simple(2, 0.25, freq_b, "sin", 0)
    if not which_turned_off[1]:
        output += fun.gen_simple(2, 0.25, 2*freq_b, "sin", -6)
    if not which_turned_off[2]:
        output += fun.gen_simple(2, 0.25, 3*freq_b, "sin", -9)
    if not which_turned_off[3]:
        output += fun.gen_simple(2, 0.25, 4*freq_b, "sin", -12)

    return output.astype(np.int16)


if __name__ == '__main__':
    freq = 1000
    ref = fun.gen_simple(2, 0.25, freq, "sin", 0)
    tones = hct(freq, 2, fs)
    choice = []

    sd.play(ref)
    sleep(2.3)
    sd.play(tones)
    choice.append(input('do you really think that pitch is the same? y/n'))

    tones = hct(freq, 2, fs, [False, True, False, True])

    sd.play(ref)
    sleep(2.3)
    sd.play(tones)
    choice.append(input('do you really think that pitch is the same now???? y/n'))

    if choice[0] == choice[1] and choice[0] == "y":
        print("You are amazing")
    else:
        print("you are not amazing")
