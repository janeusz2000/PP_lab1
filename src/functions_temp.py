import numpy as np


# GLOBAL variables
fs = 48000
max_int16 = 32767


def gen_simple_phased(duration, volume, freq, signal_type, db_offset, phase_offset):
    """
    :param duration: in seconds
    :param volume: overall volume in range 0 to 1 (ex. 0.5)
    :param freq: frequency of the signal
    :param signal_type: sin or noise
    :param db_offset: volume of the offset in dB in range from -90 to 0
    :return: numpy array with values of the signal
    """
    signal_len = int(duration * fs)

    if signal_type == "sin":
        signal_x = np.linspace(phase_offset*2*np.pi/360, 2 * np.pi * (freq / fs) * signal_len + phase_offset*2*np.pi/360, num=signal_len, endpoint=False)
        signal_y = np.sin(signal_x) * max_int16
        signal_y = signal_y.astype(np.int16)
    elif signal_type == "noise":
        signal_y = np.random.random(signal_len) * max_int16
        signal_y = signal_y.astype(np.int16)
    else:
        print('błędne parametry')
        exit()

    # In and out window generation
    window_len = int(fs / 100)
    window_x = np.linspace(0, 2 * np.pi * (25 / fs) * window_len, num=window_len, endpoint=False)
    window_in_y = np.sin(window_x)
    window_out_y = np.cos(window_x)

    # Applying window
    out_offset = len(signal_y) - window_len
    for i in range(window_len):
        signal_y[i] *= window_in_y[i]
        signal_y[i + out_offset] *= window_out_y[i]

    # Volume
    real_db_offset = 10 ** (db_offset / 20)
    signal_y = (signal_y * real_db_offset * volume).astype(np.int16)

    return signal_y
