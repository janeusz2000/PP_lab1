import src.functions_temp as fun
import random
import numpy as np
import sounddevice as sd

# GLOBAL variables
fs = 48000
max_int16 = 32767

if __name__ == '__main__':
    phase_offsets = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150] * 5
    random.shuffle(phase_offsets)
    answers = []
    for each in phase_offsets:
        Left = fun.gen_simple_phased(1, 0.8, 1000, "sin", -3.0, each)
        Right = fun.gen_simple_phased(1, 0.8, 1000, "sin", -3.0, 0)
        output = np.ndarray.transpose(np.array([Left, Right]))
        sd.play(output, fs)
        sd.wait()
        choice = input("Do you hear phase offset? y/n ")
        answers.append(str(each) + ";" + str(choice))

    f = open("output\\output_zad2.txt", "w+")
    for each in answers:
        f.write(each + "\n")
    f.close()





