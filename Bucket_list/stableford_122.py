#!/usr/bin/env python3

import sys

lines = []
par = {}
index = {}
totals_dict = {}
disq = []

score_to_par = {-7: 9,
                -6: 8,
                -5: 7,
                -4: 6,
                -3: 5,
                -2: 4,
                -1: 3,
                0: 2,
                1: 1,
                2: 0}


def stableford_points(scores, handicap):
    points = 0
    for i in range(18):
        if scores[i] == 'X':
            continue
        elif not scores[i].isdigit() and scores[i] != 'X':
            return 'Disqualified'
        else:
            free_shots = 0
            hcap = handicap
            while index[i] <= hcap:
                free_shots += 1
                hcap = hcap - 18
            net_strokes = int(scores[i]) - free_shots
            par_score = net_strokes - par[i]
            if 2 < par_score:
                par_score = 2
            points += score_to_par[par_score]
    return points


def main():
    for line in sys.stdin:
        lines.append(line.strip())

    for i in range(18):
        par[i] = int(lines[0].split()[i])
        index[i] = int(lines[1].split()[i])

    longest_name = 0
    totals_list = []

    for line in lines[2:]:
        name = ' '.join(line.split()[:-19])
        if longest_name < len(name):
            longest_name = len(name)
        handicap = int(line.split()[-19])
        scores = line.split()[-18:]
        if stableford_points(scores, handicap) == 'Disqualified':
            disq.append(name)
        else:
            totals_list.append(stableford_points(scores, handicap))
            totals_dict[stableford_points(scores, handicap)] = name

    totals_list = sorted(totals_list, reverse=True)

    for points in totals_list:
        print('{:>{}} : {:>2d}'.format(
            totals_dict[points], longest_name, points))
    for player in disq:
        print('{:>{}} : Disqualified'.format(player, longest_name))


if __name__ == '__main__':
    main()
