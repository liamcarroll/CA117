#!/usr/bin/env python3

import sys

def longest_club(table):
   len_longest_club = 0
   for line in table:
      tokens = line.split()
      i = 1
      while tokens[i].isalpha():
         i += 1
   club_name = ' '.join(tokens[1:i])
   if len_longest_club < len(club_name):
      len_longest_club = len(club_name)

def main():
   lines = []
   for line in sys.stdin:
      lines.append(line.strip())
   club_width = longest_club(lines)
   print('{} {:<{}} {:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} '.format('POS','CLUB',club_width,'P','W','D','L','GF','GA','GD','PTS'))

if __name__ == '__main__':
   main()