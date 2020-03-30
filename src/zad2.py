from src import functions
import time
import sounddevice as sd


difference = 0
ref_vol = -3
first_wav = functions.gen_signal(1, 0.5, 3000, "sin", -3)
choice = ''


if __name__ == '__main__':
    while choice != 'S':
        second_wav = functions.gen_signal(1, 0.5, 3000, "sin", ref_vol-difference)
        sd.play(first_wav, functions.fs)
        time.sleep(0.5)
        sd.play(second_wav, functions.fs)
        choice = input('Jeśli stop --> S')
        if choice == 'S':
            print(difference)
        difference += 0.5
