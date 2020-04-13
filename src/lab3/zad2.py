import src.functions_temp as fun
import random
import numpy as np
import sounddevice as sd

# GLOBAL variables
fs = 48000
max_int16 = 32767

if __name__ == '__main__':
    phase_offsets = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330] * 5
    random.shuffle(phase_offsets)
    choices = []
    for each in phase_offsets:
        Left = fun.gen_simple_phased(1, 0.8, 500, "sin", -3.0, each)
        Right = fun.gen_simple_phased(1, 0.8, 500, "sin", -3.0, 0)
        output = np.ndarray.transpose(np.array([Left, Right]))
        sd.play(output, fs)
        sd.wait()
        choice = input("Do you hear phase offset? y/n ")
        choices.append(choice)

with open("../../output/lab3/zad2_results.txt", "w") as f:
    for (choice, each) in zip(choices, phase_offsets):
        f.write(f'Różnica {each}, wcisnieto {choice}\n')



