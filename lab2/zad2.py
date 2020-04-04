import src.functions as fun
import time
import sounddevice as sd


base_freq = 1046.5
ref_wav = fun.gen_simple(1, 0.5, base_freq, "sin", -3)
delta_f = 100
choices = []
test_freq = []
for it in range(0, 10):
    sd.play(ref_wav, fun.fs)
    time.sleep(0.5)
    sd.play(fun.gen_simple(1, 0.5, base_freq + delta_f, "sin", -3))
    choice = input('Który ton byl wyzszy? [1/2]')
    choices.append(choice)
    test_freq.append(str(base_freq - delta_f))

    # Staircase method
    if choice == '1' and (base_freq > (base_freq + delta_f)):
        delta_f += 30
    elif choice == '2' and (base_freq < (base_freq + delta_f)):
        delta_f += - 30
    elif choice == '1' and (base_freq < (base_freq + delta_f)):
        delta_f += - 30
    elif choice == '2' and (base_freq > (base_freq + delta_f)):
        delta_f += 30

for a in range(0, len(test_freq)):
    print(test_freq[a] + ' ' + choices[a])

# with open("../output/lab2/zad2_results.txt", "w") as f:
#      for (test, choice) in zip(test_freq, choices):
#          f.write(f'Różnica {test}, wcisnieto {choice}\n')
#      f.close()