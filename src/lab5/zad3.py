import src.functions as fun
import numpy as np
import sounddevice as sd
from time import sleep

# Global Variables
fs = 48000
max_int16 = 32767

HCT1 = fun.gen_simple(2, 0.5, 1000, "sin", -3, dtype=np.int32)
HCT2 = fun.gen_simple(2, 0.5, 2000, "sin", -3, dtype=np.int32)
HCT3 = fun.gen_simple(2, 0.5, 3000, "sin", -3, dtype=np.int32)
HCT4 = fun.gen_simple(2, 0.5, 4000, "sin", -3, dtype=np.int32)
HCT = ((HCT1 + HCT2 + HCT3 + HCT4)/4).astype(np.int16)

sd.play(HCT, fs)
sleep(2.3)
HCT2 = fun.gen_simple(2, 0.5, 2000, "sin", -3, dtype=np.int32)
HCT3 = fun.gen_simple(2, 0.5, 3000, "sin", -3, dtype=np.int32)
HCT4 = fun.gen_simple(2, 0.5, 4000, "sin", -3, dtype=np.int32)
HCT = ((HCT2 + HCT3 + HCT4)/3).astype(np.int16)
sd.play(HCT, fs)

choice = input('Did you hear the difference in the pitch? y/n')
print(choice)