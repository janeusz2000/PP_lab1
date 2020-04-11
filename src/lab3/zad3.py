import src.functions as fun
import random
import numpy as np
import sounddevice as sd

f_dist = [2, 5, 8, 10, 15, 20, -2,  -5, -8, -10, -15, -20]
ref_wav = fun.gen_simple(1, 0.5, 1000, "sin", -3)
random_wav = [fun.gen_simple(1, 0.5, 1000 + x, "sin", -3) for x in f_dist]

if __name__ == '__main__':
    tests = f_dist * 5
    random.shuffle(tests)
    choices = []
    for test in tests:
        data = np.array([ref_wav, random_wav[f_dist.index(test)]])
        data = np.ndarray.transpose(data)
        sd.play(data, fun.fs)
        choice = input('Który był wyższy [1/2]')
        choices.append(choice)

    with open("../../output/lab3/zad3_results.txt", "w") as f:
        for (test, choice) in zip(tests, choices):
            f.write(f'Różnica {test}, wcisnieto {choice}\n')