from ctypes import *
from homu import homulib

homulib.Homu_SetSampleRate.argtypes    = [c_size_t]

def Set(sr):
    homulib.Homu_SetSampleRate(sr)

