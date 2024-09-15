from ctypes import *

libc = CDLL("libc.so.6")

printf = libc.printf
printf.argtypes = [c_char_p]

class Case(Union):
    _fields_ = [
        ("evidence_int", c_int),
        ("evidence_long", c_long),
        ("evidence_char", c_char * 4)
    ]

value = input("Enter new evidence number: ")

new_evidence = Case()
new_evidence.evidence_int = int(value)

# Print the values
print("Evidence number as an int: %i" % new_evidence.evidence_int)
print("Evidence number as a long: %i" % new_evidence.evidence_long)
print("Evidence number as a char: %s" % new_evidence.evidence_char.decode('utf-8', 'ignore'))
