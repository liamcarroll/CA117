#!/usr/bin/env python3

import sys

def convert_decimal(integer,base):
   reverse_integer = integer[::-1]
   decimal = 0
   i = 0
   while i < len(reverse_integer):
      decimal += int(reverse_integer[i]) * (int(base) ** i)
      i += 1
   print(decimal)

def main():
   for line in sys.stdin:
      [first,second] = line.strip().split()
      convert_decimal(first,second)

if __name__ == '__main__':
   main()