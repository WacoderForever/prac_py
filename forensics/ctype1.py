from ctypes import *
libc=CDLL("libc.so.6")
print(libc.time(None))