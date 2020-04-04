import src.functions as fun
import random
import time
import sounddevice as sd

f_dist = [5, 10, 15, 20, 25, -5, -10, -15, -20, -25]
ref_wav = fun.gen_simple(1, 0.5, 1000, "sin", -3)
random_wav = [fun.gen_simple(1, 0.5, 1000 + x, "sin", -3) for x in f_dist]

if __name__ == '__main__':
    tests = f_dist * 5
    random.shuffle(tests)
    choices = []
    for test in tests:
        sd.play(ref_wav, fun.fs)
        time.sleep(1.5)
        sd.play(random_wav[f_dist.index(test)], fun.fs)
        choice = input('Który był wyższy [1/2]')
        choices.append(choice)

    with open("../../output/lab2/zad1_results.txt", "w") as f:
        for (test, choice) in zip(tests, choices):
            f.write(f'Różnica {test}, wcisnieto {choice}\n')