#!/usr/bin/env python3

import sys

for line in sys.stdin:
   new_string = line.strip()[1:-1]
   if 0 < len(new_string):
      print(new_string)