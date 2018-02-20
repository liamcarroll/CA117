#!/usr/bin/env python3

def l2d(file):
    d = {}
    keys = file.readline().strip().split()
    values = file.readline().strip().split()
    for k, v in zip(keys, values):
        d[k] = int(v)
    return d