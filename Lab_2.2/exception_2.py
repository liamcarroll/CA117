#!/usr/bin/env python3


def callme02(x):
    try:
        y = 1 / x
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

print(callme02(1))
print(callme02(0))
