#!/usr/bin/env python3

import sys

lines = []
par = {}
index = {}
totals = {}

score_to_par = {-7: 9,
                -6: 8,
                -5: 7,
                -4: 6,
                -3: 5,
                -2: 4,
                -1: 3,
                0: 2,
                1: 1}


def stableford_points(scores, handicap):
    points = 0
    for i in range(18):
        if scores[i] == 'X':
            pass
        elif not scores[i].isdigit() and scores[i] != 'X':
            return 'Disqualified'
        else:
            free_shots = 0
            hcap = handicap
            while index[i] <= hcap:
                free_shots += 1
                hcap = hcap - 18
            net_strokes = int(scores[i]) - free_shots
            par_score = par[i] - net_strokes
            if 1 < par_score:
                par_score = 1
            if par_score < -7:
                par_score = -7
            points += score_to_par[par_score]
    return points


def main():
    for line in sys.stdin:
        lines.append(line.strip())
    for i in range(18):
        par[i] = int(lines[0].split()[i])
        index[i] = int(lines[1].split()[i])
    for line in lines[2:]:
        name = ' '.join(line.split()[:-19])
        handicap = int(line.split()[-19])
        scores = line.split()[-18:]
        totals[name] = stableford_points(scores, handicap)
    print(totals)
        


if __name__ == '__main__':
    main()
