import numpy as np
import sounddevice as sd
from time import sleep
import src.functions as fun
import random
# Global Variables
fs = 48000
max_int16 = 32767


def hct(freq_b, duration, fs_, ratio_, which_turned_off=[False, False, False, False]):
    output = np.zeros(duration*fs_)
    if not which_turned_off[0]:
        output += fun.gen_simple(2, 0.25, freq_b, "sin", 0)
    if not which_turned_off[1]:
        output += fun.gen_simple(2, 0.25, 2*ratio_*freq_b, "sin", -6)
    if not which_turned_off[2]:
        output += fun.gen_simple(2, 0.25, 3*ratio_*freq_b, "sin", -9)
    if not which_turned_off[3]:
        output += fun.gen_simple(2, 0.25, 4*ratio_*freq_b, "sin", -12)

    return output.astype(np.int16)


if __name__ == '__main__':
    freq = 1000
    ref = fun.gen_simple(2, 0.25, freq, "sin", 0)
    harm_ratios = np.linspace(0.5, 2.1, num=16, endpoint=False)
    choices = []
    task_two_ratios = []
    for ratio in harm_ratios:
        tones = hct(freq, 2, fs, ratio,)
        sd.play(ref)
        sleep(2.3)
        sd.play(tones)
        choice = input('do you hear the same pich y/n')
        choices.append(choice)
        if choice == "y":
            task_two_ratios.append(ratio)

    with open("../../output/lab5/zad1_results_1.txt", "w") as f:
        for (harm_ratio, choice) in zip(harm_ratios, choices):
            f.write(f'Różnica {harm_ratio}, wcisnieto {choice}\n')
        f.close()

    choices = []
    for ratio in task_two_ratios:
        delete_ind = int(random.random()*3+1)
        delete_vec = [False, False, False, False]
        delete_vec[delete_ind] = True
        htc_test = hct(freq, 2, fs, ratio, delete_vec)
        sd.play(ref)
        sleep(2.3)
        sd.play(htc_test)
        choice = input("Did you hear change in pitch? y/n")
        choices.append(choice)

    with open("../../output/lab5/zad1_results_2.txt", "w") as f:
        for (harm_ratio, choice) in zip(task_two_ratios, choices):
            f.write(f'Różnica {harm_ratio}, wcisnieto {choice}\n')
        f.close()


    print("You are amazing")
