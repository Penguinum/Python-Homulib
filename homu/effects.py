from ctypes import *
from homu import homulib

homulib.Delay_Create.argtypes     = [c_size_t]
homulib.Delay_Create.restype      = c_void_p
homulib.Delay_Start.argtypes      = [c_void_p]
homulib.Delay_SetSize.argtypes    = [c_void_p, c_double]
homulib.Delay_SetDecay.argtypes   = [c_void_p, c_double]
homulib.Delay_NextSample.argtypes = [c_void_p, c_double]
homulib.Delay_NextSample.restype  = c_double
homulib.Delay_Destroy.argtypes    = [c_void_p]


class Delay:
    def __init__(self, sample_rate):
        self.gen = homulib.Delay_Create(sample_rate)

    def __del__(self):
        self.gen = homulib.Delay_Destroy(self.gen)
        
    def set_width(self, s):
        homulib.Delay_SetSize(self.gen, s)

    def set_decay(self, value):
        homulib.Delay_SetDecay(self.gen, value)

    def start(self):
        homulib.Delay_Start(self.gen)

    def next_sample(self, s):
        return homulib.Delay_NextSample(self.gen, s)

