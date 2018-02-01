#!/usr/bin/env python3

import sys

def capitalise_all(s):
   words = s.split()
   new_words = []
   for word in words:
      new_words.append(word.capitalize())
   print(' '.join(new_words))

def main():
   for line in sys.stdin:
      line = line.strip()
      capitalise_all(line)

if __name__ == '__main__':
   main()