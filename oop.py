import sys
import struct

class Worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def last(self):
            return self.name.split()[-1]
    def inc(self,pay):
         self.pay = (int)((110/100)*pay)

Bob=Worker('Bob Jun',6000)
print(Bob.last())
Bob.inc(Bob.pay)
print(Bob.pay)