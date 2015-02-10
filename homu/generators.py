from ctypes import *
from homu import homulib

homulib.KarplusStrong_Create.restype      = c_void_p
homulib.KarplusStrong_Start.argtypes      = [c_void_p, c_double]
homulib.KarplusStrong_NextSample.argtypes = [c_void_p]
homulib.KarplusStrong_NextSample.restype  = c_double
homulib.KarplusStrong_Destroy.argtypes    = [c_void_p]

homulib.Sinewave_Create.restype           = c_void_p
homulib.Sinewave_Start.argtypes           = [c_void_p, c_double]
homulib.Sinewave_NextSample.argtypes      = [c_void_p]
homulib.Sinewave_NextSample.restype       = c_double
homulib.Sinewave_Destroy.argtypes         = [c_void_p]

homulib.Triangle_Create.restype           = c_void_p
homulib.Triangle_Start.argtypes           = [c_void_p, c_double]
homulib.Triangle_SetWidth.argtypes        = [c_void_p, c_double]
homulib.Triangle_NextSample.argtypes      = [c_void_p]
homulib.Triangle_NextSample.restype       = c_double
homulib.Triangle_Destroy.argtypes         = [c_void_p]

homulib.BrownNoise_Create.restype         = c_void_p
homulib.BrownNoise_Start.argtypes         = [c_void_p, c_double]
homulib.BrownNoise_NextSample.argtypes    = [c_void_p]
homulib.BrownNoise_NextSample.restype     = c_double
homulib.BrownNoise_Destroy.argtypes       = [c_void_p]

homulib.WhiteNoise_Create.restype         = c_void_p
homulib.WhiteNoise_Start.argtypes         = [c_void_p, c_double]
homulib.WhiteNoise_NextSample.argtypes    = [c_void_p]
homulib.WhiteNoise_NextSample.restype     = c_double
homulib.WhiteNoise_Destroy.argtypes       = [c_void_p]

homulib.PinkNoise_Create.restype          = c_void_p
homulib.PinkNoise_Start.argtypes          = [c_void_p, c_double]
homulib.PinkNoise_NextSample.argtypes     = [c_void_p]
homulib.PinkNoise_NextSample.restype      = c_double
homulib.PinkNoise_Destroy.argtypes        = [c_void_p]


class KarplusStrong:
    def __init__(self):
        self.gen = homulib.KarplusStrong_Create()

    def __del__(self):
        self.gen = homulib.KarplusStrong_Destroy(self.gen)
        

    def start(self, frequency):
        homulib.KarplusStrong_Start(self.gen, frequency)

    def next_sample(self):
        return homulib.KarplusStrong_NextSample(self.gen)


class Sinewave:
    def __init__(self):
        self.gen = homulib.Sinewave_Create()

    def __del__(self):
        self.gen = homulib.Sinewave_Destroy(self.gen)
        
    def start(self, frequency):
        homulib.Sinewave_Start(self.gen, frequency)

    def next_sample(self):
        return homulib.Sinewave_NextSample(self.gen)


class Triangle:
    def __init__(self):
        self.gen = homulib.Triangle_Create()

    def __del__(self):
        self.gen = homulib.Triangle_Destroy(self.gen)
        
    def start(self, frequency):
        homulib.Triangle_Start(self.gen, frequency)

    def set_width(self, width):
        homulib.Triangle_SetWidth(self.gen, width)

    def next_sample(self):
        return homulib.Triangle_NextSample(self.gen)


class BrownNoise:
    def __init__(self):
        self.gen = homulib.BrownNoise_Create()

    def __del__(self):
        self.gen = homulib.BrownNoise_Destroy(self.gen)
        
    def start(self, frequency):
        homulib.BrownNoise_Start(self.gen, frequency)

    def next_sample(self):
        return homulib.BrownNoise_NextSample(self.gen)


class WhiteNoise:
    def __init__(self):
        self.gen = homulib.WhiteNoise_Create()

    def __del__(self):
        self.gen = homulib.WhiteNoise_Destroy(self.gen)
        

    def start(self, frequency):
        homulib.WhiteNoise_Start(self.gen, frequency)

    def next_sample(self):
        return homulib.WhiteNoise_NextSample(self.gen)


class PinkNoise:
    def __init__(self):
        self.gen = homulib.PinkNoise_Create()

    def __del__(self):
        self.gen = homulib.PinkNoise_Destroy(self.gen)
        
    def start(self, frequency):
        homulib.PinkNoise_Start(self.gen, frequency)

    def next_sample(self):
        return homulib.PinkNoise_NextSample(self.gen)

