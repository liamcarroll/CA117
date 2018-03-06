#!/usr/bin/env python3

import sys

def main():
    food_cal = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            foodstuff, calories = line.strip().split()
            food_cal[foodstuff] = int(calories)

    total_cals_per_person = {}
    for line in sys.stdin:
        line = line.strip().split(',')
        name = line[0]
        consumed_food = line[1:]

        total = 0
        for food in consumed_food:
            try:
                total += food_cal(food)
            except KeyError:
                total += 100
        total_cals_per_person[name] = total

    