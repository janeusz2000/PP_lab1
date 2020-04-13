import src.functions_temp as fun
import random
import numpy as np
import sounddevice as sd

# GLOBAL variables
fs = 48000
max_int16 = 32767

if __name__ == '__main__':
    pitch_offset = [0, 2, 5, 8, 10, 15, 20, -2,  -5, -8, -10, -15, -20]*5
    random.shuffle(pitch_offset)
    choices = []
    for each in pitch_offset:
        Left = fun.gen_simple_phased(1, 0.8, 600+each, "sin", -3.0, 0)
        Right = fun.gen_simple_phased(1, 0.8, 600, "sin", -3.0, 0)
        output = np.ndarray.transpose(np.array([Left, Right]))
        sd.play(output, fs)
        choice = input("Do you hear binaural beats? y/n ")
        choices.append(choice)

    with open("../../output/lab3/zad4_results.txt", "w") as f:
        for (each, choice) in zip(pitch_offset, choices):
            f.write(f'Różnica {each}, wcisnieto {choice}\n')