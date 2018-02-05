#!/usr/bin/env python3

import sys

vowels = ['a','e','i','o','u']

def plural(noun):
   if noun[-2:] in ['ch','sh'] or noun[-1] in ['x','s','z','o']:
      return noun + 'es'
   elif noun[-2] not in vowels and noun[-1] == 'y':
      return noun[:-1] + 'ies'
   elif noun[-1] == 'f':
      return noun[:-1] + 'ves'
   elif noun[-2:] == 'fe':
      return noun[:-2] + 'ves'
   else:
      return noun + 's'

def main():
    for line in sys.stdin:
        word = line.strip()
        print(plural(word))

if __name__ == '__main__':
   main()