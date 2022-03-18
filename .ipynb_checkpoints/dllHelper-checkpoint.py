import glob
import ctypes
def loadDll(path):
    dll1 = glob.glob(path)
    for dll in dll1:
        try:
            ctypes.WinDLL(dll)
        except:
            pass