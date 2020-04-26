import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep


# Global Variables
fs = 48000
max_int16 = 32767

if __name__ == '__main__':

    ref = fun.gen_simple(1, 0.2, 0, "noise", 0)
    choices = []
    tests = []
    user_input = 'y'
    offset = -6
    while user_input == 'y':
        left = np.copy(ref)
        left[int(fs / 4):int(3 * fs / 4)] += fun.gen_simple(0.5, 0.2, 1000, "sin", offset)
        right = np.zeros(len(left), dtype=np.int16)

        output = np.array((left, right)).T
        sd.play(output, fs)
        sleep(1.2)
        user_input = input("Did you hear the tone? y/n ")

        offset -= 1
    print('\n' + str(offset))


