#!/usr/bin/env python3

import sys

def contains(chars, s):
   for c in chars:
      if c in s:

def main():
   for line in sys.stdin:
      [left,right] = line.strip().split()
      print(contains(left,right))