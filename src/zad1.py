from src import functions
import random
import time
import sounddevice as sd

distances = [-3.5, -4.5, -5, -6, -8]
ref_wav = functions.gen_signal(0.2, 0.5, 1000, "sin", -3)
random_wav = [functions.gen_signal(0.2, 0.5, 1000, "sin", x) for x in distances]

if __name__ == '__main__':
    tests = distances * 10
    random.shuffle(tests)
    choices = []
    for test in tests:
        sd.play(ref_wav, functions.fs)
        time.sleep(1)
        sd.play(random_wav[distances.index(test)], functions.fs)
        choice = input('Roznica? [Y/N]')
        choices.append(choice)

    with open("../output/Output1.txt", "w") as f:
        for (test, choice) in zip(tests, choices):
            f.write(f'Różnica {test}, wcisnieto {choice}\n')
    f.close()