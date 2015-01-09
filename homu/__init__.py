from ctypes import *
import platform

os = platform.system()
if os == "Windows":
    libname = "homulib.dll"
elif os == "Linux":
    libname = "libhomulib.so"
else:
    print("Sorry, your OS is not supported now")
    exit(1)

cdll.LoadLibrary(libname)
homulib = CDLL(libname)
