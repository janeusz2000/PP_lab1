from src import functions
import time
import sounddevice as sd


difference = 0
ref_dur = 2
first_wav = functions.gen_signal(2, 0.5, 3000, "sin", -3)
choice = ''


if __name__ == '__main__':
    while choice != 'YN':
        second_wav = functions.gen_signal(ref_dur + difference, 0.5, 3000, "sin", -3)
        sd.play(first_wav, functions.fs)
        time.sleep(0.3)
        sd.play(second_wav, functions.fs)
        time.sleep(0.3)
        sd.play(first_wav, functions.fs)
        choice = input('Różnica w głośności tonów --> [Y/N]')
        if choice == 'Y':
            print(ref_dur + difference)
        difference += 0.5