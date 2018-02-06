#!/usr/bin/env python3

import sys

totals = {'total_0': 0,
          'total_1': 0,
          'total_2': 0,
          'total_3': 0,
          'total_4': 0,
          'total_5': 0,
          'total_6': 0,
          'total_7': 0,
          'total_8': 0,
          'total_9': 0}


ranks = {0: 'nothing',
         1: 'one pair',
         2: 'two pairs',
         3: 'three of a kind',
         4: 'a straight',
         5: 'a flush',
         6: 'a full house',
         7: 'four of a kind',
         8: 'a straight flush',
         9: 'a royal flush'}


def main():
    for line in sys.stdin:
        rank = line.strip()[-1]
        totals['total_{}'.format(rank)] += 1

    total_hands = 0
    for key in totals:
        total_hands += totals[key]

    for i in range(10):
        frequency = totals['total_{}'.format(i)]
        probability = (frequency / total_hands) * 100
        print('The probability of {} is {:.4f}%'.format(ranks[i], probability))

if __name__ == '__main__':
    main()
