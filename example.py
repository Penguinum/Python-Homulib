#!/usr/bin/env python3

from homu.generators import KarplusStrong
from homu.envelopes import ADSR
from homu.effects import Delay
import homu.samplerate
import numpy as np
import scipy.io.wavfile as wavfile


def main():
    sample_rate = 44100
    homu.samplerate.Set(sample_rate)
    gen = KarplusStrong()
    gen.start(400)

    rev = Delay()
    rev.set_size(0.5)
    rev.set_decay(0.5)
    rev.start()

    adsr = ADSR()
    adsr.set_attack(0.01)
    adsr.set_decay(0.2)
    adsr.set_sustain(0.7)
    adsr.set_release(0.2)
    adsr.start()

    samples = []

    while (not adsr.finished()):
        if (adsr.seconds_played() >= 40):
            adsr.stop_sustain()

        s = rev.next_sample(gen.next_sample()) * adsr.next_sample()
        samples.append(s)

    wavfile.write('test.wav', sample_rate, np.array(samples))


if __name__ == "__main__":
    main()
