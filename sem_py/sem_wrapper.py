import ctypes
from numpy import ctypeslib


def sem(data, n_iter, n_components, sem_dll_libname, sem_dll_loader_path):

    leb = ctypeslib.load_library(libname=sem_dll_libname, loader_path=sem_dll_loader_path)
    n = len(data)

    leb.sem.argtypes = [ctypes.c_int, ctypes.c_int,
                        ctypeslib.ndpointer(dtype=data.dtype, ndim=1, flags='C_CONTIGUOUS'),
                        ctypes.c_int]
    leb.sem.restype = ctypes.POINTER(ctypes.c_double)
    result = leb.sem(n_iter, n_components, data, n)
    result_ = ctypeslib.as_array(result, shape=((n_components * 2 + 2),))

    return result_
