import sys
import numpy as np


class Operation:

    def __init__(self):
        self.op_code = []

    def setter(self):
        pass
    def getter(self):
        pass

    code = property(getter, setter)


bin_file = open("test1.bin","w")
bin_file.write(00000000001000100001100000100000)
