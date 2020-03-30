import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import random
# GLOBAL Variables
fs = 48000


def gen_signal(_duration, _volume, f, _signal_type, _db_offset):
    """

    :param _duration: in seconds
    :param _volume: overall volume in range 0 to 1 (ex. 0.5)
    :param f: frequency of the signal
    :param _signal_type: sin or noise
    :param _db_offset: volume of the offset in dB in range from -90 to 0
    :return: numpy array with values of the signal
    """
    signal_len = int(_duration * fs)
    # x_os = np.ones(int(_duration * fs))

    if _signal_type == "sin":
        # SINUS gen
        y_os = np.linspace(0, 2 * np.pi * (f / fs) * signal_len, num=signal_len)
        # for it in range(0, np.size(x_os)):
        #     x_os[it] = 2 * np.pi * (f / fs) * it
        # y_os = np.sin(x_os)
        #
        # # NORM
        # y_os = y_os*32767

    if _signal_type == "noise":
        # NOISE gen + NORM
        y_os = np.random.random(signal_len)
        # y_os = np.ones(int(_duration * fs))
        # for it in range(0, np.size(x_os)):
        #     y_os[it] = random.randrange(-32767, 32767)

    # WINDOW in and out gen
    x_win = np.linspace(0, 2 * np.pi * (25 / fs) * int(fs / 100), num=int(fs / 100))
    # x_win = np.ones(int(fs/100))
    # for it in range(0, np.size(x_win)):
    #     x_win[it] = 2*np.pi*(25/fs)*it

    y_win_in = np.sin(x_win)
    y_win_out = np.cos(x_win)

    # APPLYING WINDOW
    for it in range(0, np.size(y_win_in)):
        # y_os[it] = y_os[it]*y_win_in[it]
        y_os[it] *= y_win_in[it]

    for it in range(np.size(y_os)-np.size(y_win_out), np.size(y_os)):
        y_os[it] = y_os[it]*y_win_out[it-np.size(y_os)+np.size(y_win_out)]

    # VOLUME
    real_db_offset = 10**(_db_offset/20)
    y_os *= _volume * real_db_offset
    # for it in range(0, np.size(y_os)):
    #     y_os[it] = int(y_os[it]*_volume*real_db_offset)

    return y_os


def create_wav(_name, _data):
    return wav.write(_name, fs, _data)


if __name__ == '__main__':
    A = gen_signal(0.2, 0.5, 1000, "noise", -6)
    A.astype(np.int16)
    time = np.linspace(0., np.size(A), num=np.size(A), endpoint=False)
    plt.plot(time, A)
    plt.show()
    create_wav("test4.wav", A)
    print("END")
