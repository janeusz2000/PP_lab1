import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import random
# GLOBAL Variables
fs = 48000


def sin_signal(_duration, _volume, f, _signal_type, _dB_offset):
    """

    :param _duration: in seconds
    :param _volume: overall volume in range 0 to 1 (ex. 0.5)
    :param f: frequency of the signal
    :param _signal_type: sin or noise
    :param _dB_offset: volume of set in dB in range -90 to 0
    :return: numpy array with values of the signal
    """

    x_os = np.ones(int(_duration * fs))

    if _signal_type == "sin":
        # SINUS gen
        for it in range(0, np.size(x_os)):
            x_os[it] = 2 * np.pi * f / fs * it
        y_os = np.sin(x_os)

        # NORM
        for it in range(0, np.size(x_os)):
            y_os[it] = y_os[it]*32767

    if _signal_type == "noise":
        # NOISE gen + NORM
        y_os = np.ones(int(_duration * fs))
        for it in range(0, np.size(x_os)):
            y_os[it] = random.randrange(-32767, 32767)

    # WINDOW in and out gen
    x_win = np.ones(int(fs/100))
    for it in range(0, np.size(x_win)):
        x_win[it] = 2*np.pi*25/fs*it

    y_win_in = np.sin(x_win)
    y_win_out = np.cos(x_win)

    # APPLYING WINDOW
    for it in range(0, np.size(y_win_in)):
        y_os[it] = y_os[it]*y_win_in[it]

    for it in range(np.size(y_os)-np.size(y_win_out), np.size(y_os)):
        y_os[it] = y_os[it]*y_win_out[it-np.size(y_os)+np.size(y_win_out)]

    # VOLUME
    real_dB_offset = 10**(_dB_offset/20)
    for it in range(0, np.size(y_os)):
        y_os[it] = int(y_os[it]*_volume*real_dB_offset)

    return y_os

def create_wav(_name, _data):
    return wav.write(_name,fs,_data)

A = sin_signal(0.2, 0.5, 1000, "noise", -6)
A.astype(np.int16)
time = np.linspace(0., np.size(A), num=np.size(A), endpoint=False)
plt.plot(time, A)
plt.show()
create_wav("test3.wav", A)
print("END")