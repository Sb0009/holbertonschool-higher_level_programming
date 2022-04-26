#!/usr/bin/python3
import dis


def magic_calculation(a, b, c):
    if (a < b):
        return (False)
    elif (c > b):
        return (False)
    else:
        return (a + b)
    return (a * b)


dis.dis(magic_calculation)
