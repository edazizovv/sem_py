import os
import sys


d = os.path.dirname(os.path.realpath(__file__))
if d not in sys.path:
    sys.path.append(d)


from test_data_generator import gen2
from sem_wrapper import sem


#data = gen2(0.5, 2.2, 3.9, 1.4, 1.7)
data = gen2(0.5, 1.0, 2.0, 2.0, 1.0)




result = sem(data=data, n_iter=100, n_components=2,
             sem_dll_libname='sem_cpp.dll', sem_dll_loader_path=d)


