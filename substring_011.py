#!/usr/bin/env python3

import sys

def is_substring(substring, string):
   if substring in string:
      return True
   else:
      return False

def main():
   for line in sys.stdin:
      [possible_sub, s] = line.strip().lower().split()
      print(is_substring(possible_sub, s))

if __name__ == '__main__':
   main()