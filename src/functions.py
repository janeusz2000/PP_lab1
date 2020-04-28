import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# GLOBAL variables
fs = 48000
max_int16 = 32767


# Gen NORMAL Signal
def gen_simple(duration, volume, freq, signal_type, db_offset, dtype=np.int16):
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
        signal_x = np.linspace(0, 2 * np.pi * (freq / fs) * signal_len, num=signal_len, endpoint=False)
        signal_y = np.sin(signal_x) * max_int16
        # signal_y = signal_y.astype(np.int16)
    elif signal_type == "noise":
        signal_y = np.random.random(signal_len) * max_int16
        # signal_y = signal_y.astype(np.int16)
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
    # signal_y = (signal_y * real_db_offset * volume).astype(np.int16)
    signal_y = signal_y * real_db_offset * volume

    return signal_y.astype(dtype)


# Gen Modulated
def get_simple_FM(duration, volume, freq_base, freq_mod, depth, db_offset):
    """
    :param duration: in seconds
    :param volume: overall volume in range 0 to 1 (ex. 0.5)
    :param freq_base: frequency of the signal
    :param freq_mod: frequency of the modulator signal
    :param depth: intesivity of the modulation
    :param db_offset: volume of the offset in dB in range from -90 to 0
    :return: numpy array with values of the signal
    """

    signal_len = int(duration * fs)

    # Modulator
    x_mod = np.linspace(0, 2 * np.pi * (freq_mod / fs) * signal_len, num=signal_len, endpoint=False)
    x_base = np.linspace(0, 2 * np.pi * (freq_base / fs) * signal_len, num=signal_len, endpoint=False)
    # BaseSignal
    y_base = np.sin(x_base + depth * np.sin(x_mod))

    # In and out window generation
    window_len = int(fs / 100)
    window_x = np.linspace(0, 2 * np.pi * (25 / fs) * window_len, num=window_len, endpoint=False)
    window_in_y = np.sin(window_x)
    window_out_y = np.cos(window_x)

    # Applying window
    out_offset = np.size(y_base) - window_len
    for i in range(window_len):
        y_base[i] *= window_in_y[i]
        y_base[i + out_offset] *= window_out_y[i]

    real_db_offset = 10 ** (db_offset / 20)
    output = (y_base * real_db_offset * volume * max_int16).astype(np.int16)
    return output


def create_wav(_name, _data):
    return wav.write(_name, fs, _data)


if __name__ == '__main__':
    A = gen_simple(0.2, 0.5, 1000, "noise", -6)
    A.astype(np.int16)
    time = np.linspace(0., np.size(A), num=np.size(A), endpoint=False)
    plt.plot(time, A)
    plt.show()
    create_wav("test4.wav", A)
    print("END")
