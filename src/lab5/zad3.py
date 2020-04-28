import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep

# Global Variables
fs = 48000
max_int16 = 32767

HCT = fun.gen_simple(2, 0.5, 1000,"sin",0)
ref = fun.gen_simple(2, 0.5, 1000,"sin",0)
HCT += fun.gen_simple(2, 0.5, 2000, "sin", -6)
HCT += fun.gen_simple(2, 0.5, 3000, "sin", -9)
HCT += fun.gen_simple(2, 0.5, 4000, "sin", -12)
sd.play(ref, fs)
sleep(2.3)
sd.play(HCT, fs)
HCT = fun.gen_simple(2, 0.5, 2000, "sin", -6)
HCT += fun.gen_simple(2, 0.5, 3000, "sin", -9)
HCT += fun.gen_simple(2, 0.5, 4000, "sin", -12)
sd.play(ref, fs)
sleep(2.3)
sd.play(HCT, fs)

choice = input('Did you hear the difference in the pitch? y/n')
print(choice)