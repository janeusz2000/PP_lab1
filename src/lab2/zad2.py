import src.functions as fun
import time
import sounddevice as sd


base_freq = 1000
ref_wav = fun.gen_simple(1, 0.5, base_freq, "sin", -3)
delta_f = 15
choices = []
test_freq = []
correct_ans = []
prev_ans_correct = False

for _ in range(0, 50):
    new_wav = fun.gen_simple(1, 0.5, base_freq + delta_f, "sin", -3)

    sd.play(ref_wav, fun.fs)
    time.sleep(1.5)
    sd.play(new_wav, fun.fs)

    choice = input('Który ton byl wyzszy? [1/2]')
    choices.append(choice)
    test_freq.append(delta_f)

    # print(f'Base freq: {base_freq}, delta: {delta_f}, choises: {choices}, test_freq: {test_freq}')

    if base_freq > (base_freq + delta_f):
        correct = '1'
    else:
        correct = '2'

    user_correct = choice == correct

    if user_correct and prev_ans_correct:
        if correct == '1':
            delta_f += 4
        else:
            delta_f -= 4

    if not user_correct:
        if correct == '1':
            delta_f -= 4
        else:
            delta_f += 4

    correct_ans.append(user_correct)
    prev_ans_correct = user_correct

with open("../../output/lab2/zad2_results.txt", "w") as f:
    for (test, ans) in zip(test_freq, correct_ans):
        f.write(f'Różnica {test}, odpowiedz {ans}\n')