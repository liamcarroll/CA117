#!/usr/bin/env python3


def callme01(x):
    y = None
    try:
        y = 1 / x
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

print(callme01(1))
print(callme01(0))
