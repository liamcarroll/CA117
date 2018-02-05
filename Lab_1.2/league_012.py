#!/usr/bin/env python3

import sys

def longest_club(table):
   longest = 0
   for line in table:
      tokens = line.split()
      club_name = ' '.join(tokens[1:-8])
      if longest < len(club_name):
         longest = len(club_name)
   return longest

def main():
   table = []
   for line in sys.stdin:
      table.append(line.strip())
   club_width = longest_club(table)
   print('{} {:<{}} {:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}'.format('POS','CLUB',club_width,'P','W','D','L','GF','GA','GD','PTS'))
   
   for line in table:
      tokens = line.split()
      print(tokens)
      club_name = tokens[1:-8]
      print('{:>3d} {:<{}} {:>2d} {:>3d} {:>3d} {:>3d} {:>3d} {:>3d} {:>3d} {:>3d}'.format(tokens[0], club_name, club_width, tokens[-8], tokens[-7], tokens[-6], tokens[-5], tokens[-4], tokens[-3], tokens[-2], tokens[-1]))

if __name__ == '__main__':
   main()