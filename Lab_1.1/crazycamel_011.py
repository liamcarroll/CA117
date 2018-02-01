#!/usr/bin/env python3

import sys

def capitalise_all_last(s):
   words = s.split()
   new_words = []
   for word in words:
      rev_cap = word[::-1].capitalize()
      new_words.append(rev_cap[::-1])
   print(' '.join(new_words))

def main():
   for line in sys.stdin:
      line = line.strip()
      capitalise_all_last(line)

if __name__ == '__main__':
   main()