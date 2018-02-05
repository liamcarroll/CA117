#!/usr/bin/env python3

import sys
from math import pi

n = int(sys.argv[1])
print('{:.{}f}'.format(pi,n))