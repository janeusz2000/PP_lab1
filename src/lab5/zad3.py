from src import functions as fun
import numpy as np
import sounddevice as sd
from time import sleep


def add_with_normalize(*args, max_value=0, dtype=np.float):
    if max_value == 0:
        for signal in args:
            if max(signal) > max_value:
                max_value = max(signal)

    signal_sum = sum(list(args))
    normalize_factor = max(signal_sum) / max_value
    normalized_signal = signal_sum / normalize_factor

    # print(f'Adding {len(args)} signals with max_value = {max_value}, normalize_factor = {normalize_factor}')
    # print(f'Summed signal with max value = {max(signal_sum)}, after normalization max value = {max(normalized_signal)}')

    return normalized_signal.astype(dtype)


H1 = fun.gen_simple(2, 0.5, 1000, "sin", -3, dtype=np.float)
H2 = fun.gen_simple(2, 0.5, 2000, "sin", -3, dtype=np.float)
H3 = fun.gen_simple(2, 0.5, 3000, "sin", -3, dtype=np.float)
H4 = fun.gen_simple(2, 0.5, 4000, "sin", -3, dtype=np.float)

# First tone
HCT1 = add_with_normalize(H1, H2, H3, H4, max_value=max(H1), dtype=np.int16)

# Second tone
HCT2 = add_with_normalize(H2, H3, H4, max_value=max(H1), dtype=np.int16)

# Play sound
sd.play(HCT1, fun.fs, blocking=True)
sleep(0.3)
sd.play(HCT2, fun.fs, blocking=True)
