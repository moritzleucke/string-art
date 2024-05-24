import ctypes 
import pathlib 
import numpy as np

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "build" / "libstringart.so"
    c_lib = ctypes.CDLL(libname)

    c_lib.cmult.restype = ctypes.c_double

    ptr = np.array([1.2, 2.2]).astype(np.float64).ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    print(c_lib.cmult(ctypes.c_int(6), ptr))
    print(np.float64(6*3.3))