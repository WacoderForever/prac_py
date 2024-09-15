from ctypes import *

# Load the C standard library
libc = CDLL("libc.so.6")

printf = libc.printf
printf.argtypes = [c_char_p]

format_str = b"An integer is: %d, A float is: %.2f\n"  # Note the use of 'b' for a byte string
int_arg = c_int(567)
float_arg = c_double(88.906789)

printf(format_str, int_arg, float_arg)
