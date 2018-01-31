#!/usr/bin/env python3

import sys

def capitalise(s):
   t = s[0].upper() + s[1:-1] + s[-1].upper()
   return t

def main():
   for line in sys.stdin:
      line = line.strip()
      if 2 <= len(line):
         print(capitalise(line))

if __name__ == '__main__':
   main()