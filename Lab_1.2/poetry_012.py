#!/usr/bin/env python3

import sys

lines = []
len_longest = 0 
for line in sys.stdin:
   line = line.strip()
   lines.append(line)
   if len_longest < len(line):
      len_longest = len(line)


for line in lines:
   print('{:^{}s}'.format(line, len_longest))