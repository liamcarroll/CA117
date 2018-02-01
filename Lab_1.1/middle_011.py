#!/usr/bin/env python3

import sys

def middle_character(s):
   if len(s) % 2 == 1:
      print(s[len(s) // 2])
   else:
      print('No middle character!')

def main():
   for line in sys.stdin:
      middle_character(line.strip())

if __name__ == '__main__':
   main()