from ctypes import *
from homu import homulib

homulib.ADSR_Create.argtypes        = [c_size_t]
homulib.ADSR_Create.restype         = c_void_p
homulib.ADSR_Destroy.argtypes       = [c_void_p]
homulib.ADSR_Start.argtypes         = [c_void_p]
homulib.ADSR_SetAttack.argtypes     = [c_void_p, c_double]
homulib.ADSR_SetDecay.argtypes      = [c_void_p, c_double]
homulib.ADSR_SetSustain.argtypes    = [c_void_p, c_double]
homulib.ADSR_SetRelease.argtypes    = [c_void_p, c_double]
homulib.ADSR_NextSample.argtypes    = [c_void_p]
homulib.ADSR_NextSample.restype     = c_double
homulib.ADSR_SecondsPlayed.argtypes = [c_void_p]
homulib.ADSR_SecondsPlayed.restype  = c_double
homulib.ADSR_Finished.argtypes      = [c_void_p]
homulib.ADSR_Finished.restype       = c_int
homulib.ADSR_StopSustain.argtypes   = [c_void_p]

class ADSR:
    def __init__(self, sample_rate):
        self.adsr = homulib.ADSR_Create(sample_rate)
    
    def __del__(self):
        homulib.ADSR_Destroy(self.adsr)

    def start(self):
        homulib.ADSR_Start(self.adsr)

    def set_attack(self, v):
        homulib.ADSR_SetAttack(self.adsr, v)

    def set_decay(self, v):
        homulib.ADSR_SetDecay(self.adsr, v)

    def set_sustain(self, v):
        homulib.ADSR_SetSustain(self.adsr, v)

    def set_release(self, v):
        homulib.ADSR_SetRelease(self.adsr, v)

    def next_sample(self):
        return homulib.ADSR_NextSample(self.adsr)

    def seconds_played(self):
        return homulib.ADSR_SecondsPlayed(self.adsr)

    def finished(self):
        return homulib.ADSR_Finished(self.adsr)

    def stop_sustain(self):
        homulib.ADSR_StopSustain(self.adsr)

