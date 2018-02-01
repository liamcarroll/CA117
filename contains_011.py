#!/usr/bin/env python3

import sys

def contains(chars,s):
   for c in chars:
      if c in s:
         s = s.replace(c,'',1)
      else:
         return False
   return True

def main():
   for line in sys.stdin:
      [left,right] = line.strip().lower().split()
      print(contains(left,right))

if __name__ =='__main__':
   main()