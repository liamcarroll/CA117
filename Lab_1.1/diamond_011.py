#!/usr/bin/env python3

import sys

def diamond(size):
   for i in range(-size+1,size):
      i = abs(i)
      print(end=' ' * i)
      print(' '.join(['*'] * (size-i)))

def main():
   n = int(sys.argv[1])
   diamond(n)

if __name__ == '__main__':
   main()