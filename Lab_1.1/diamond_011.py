#!/usr/bin/env python3

def diamond(middle_asterisks):
   i = 0
   while i < n - 1:
      print((' ' * n - i - 1) + ('*' * i + 1), end='')

def main():
   n = int(sys.argv[1])
   diamond(n)

if __name__ = '__main__':
   main()