import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep


# Global Variables
fs = 48000
max_int16 = 32767

if __name__ == '__main__':
    volume_offsets = np.linspace(0, -12, num=20, endpoint=False)
    ref = fun.gen_simple(1, 0.3, 0, "noise", 0)
    choices = []
    tests = []
    for offset in volume_offsets:
        left = np.copy(ref)
        left[int(fs / 4):int(3 * fs / 4)] += fun.gen_simple(0.5, 0.3, 1000, "sin", offset)
        right = np.zeros((np.size(left))).astype(np.int16)

        output = np.ndarray.transpose(np.array((left, right)))
        sd.play(output, fs)
        sleep(1.2)
        choice = input("Did you hear the tone? y/n ")
        choices.append(choice)
        tests.append(offset)

    with open("../../output/lab4/zad1_results.txt", "w") as f:
        for (test, choice) in zip(tests, choices):
            f.write(f'Różnica {test}, wcisnieto {choice}\n')


