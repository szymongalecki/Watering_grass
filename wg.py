"""
Watering Grass - https://itu.kattis.com/problems/grass

'n' sprinklers are installed in a horizontal strip of grass 
'l' meters long and  
'w' meters wide. 

Each sprinkler is installed at the horizontal center line of the strip. 
For each sprinkler we are given:
    - its position as the distance from the left end of the center line 
    - its radius of operation.

Q: What is the minimum number of sprinklers to turn on in order to water the entire strip of grass?
"""
import math

while True:
    try:
        n, end, w = [int(_) for _ in input().split()]
        # print(n, end, w)
        sprinkler = dict()
        coverage = list()
    except (EOFError, ValueError):
        break

    for _ in range(n):
        # sprinkler's position and radius
        x, r = [int(_) for _ in input().split()]

        # useless sprinklers are excluded
        if 2 * r <= w:
            continue

        # covered rectangular area, left and right from position
        k = math.sqrt(math.pow(r, 2) - math.pow(w / 2, 2))
        coverage.append([x - k, x + k])

    # all sprinklers were useless
    if not coverage:
        print(-1)
        continue

    # sort by left side coverage
    coverage.sort()

    # parameters
    s = 1
    l_used, r_used = coverage[0]
    l_best, r_best = 0, 0

    for i, (l, r) in enumerate(coverage):
        # previously used sprinkler reached the end of grass strip
        if r_used > end:
            print(s)
            break

        # first sprinkler can't cover the left side of grass strip
        if i == 0 and l > 0:
            print(-1)
            break

        # last sprinkler can't cover the right side of grass strip
        if i == len(coverage) - 1 and r < end:
            print(-1)
            break

        # current sprinkler is compatible with previously used sprinkler
        if l <= r_used:
            if r > end:
                print(s + 1)
                break

            # current sprinkler has the biggest right side coverage
            if r > r_best:
                l_best, r_best = l, r

        # current sprinkler is uncompatible with previously used sprinkler
        else:
            # current sprinkler is compatible with the best sprinkler
            if l <= r_best:
                s += 1
                l_used, r_used = l_best, r_best
                l_best, r_best = l, r

            # current sprinkler is uncompatible - unbreachable gap
            else:
                print(-1)
                break

"""
    Previous approach

    # start with no sprinklers, on the left side of the strip
    s = 1
    left, right = coverage.pop(0)
    if left > 0:
        print(-1)
        break

    # choose the sprinkler overlapping with previous one, with the biggest coverage
    while coverage:

        # end was reached, finish
        if right >= end:
            print(s)
            break

        # choose compatible sprinklers, do not include yourself
        compatible = [
            [l, r] for l, r in coverage if l <= right and l != left and r != right
        ]

        # detect gap and finish or proceed
        if compatible:
            left, right = max(compatible, key=lambda x: x[1])
            f = coverage.index([left, right])
            coverage = coverage[f:]
            s += 1
        else:
            print("-1")
            break
    """
