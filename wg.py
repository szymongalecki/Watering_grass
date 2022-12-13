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
        # print(n, l, w)
        sprinkler = dict()
        coverage = list()
    except (EOFError, ValueError):
        break

    for _ in range(n):
        # sprinkler's position and radius
        x, r = [int(_) for _ in input().split()]

        # don't add useless sprinkler
        if 2 * r <= w:
            continue

        # covered rectangular area, left and right from position
        k = math.sqrt(math.pow(r, 2) - math.pow(w / 2, 2))
        coverage.append([x - k, x + k])
        sprinkler[x] = r

    # sort by left side coverage
    coverage.sort()

    # # start with no sprinklers, on the left side of the strip
    # s = 1
    # left, right = coverage.pop(0)
    # if left > 0:
    #     print(-1)
    #     break

    # # choose the sprinkler overlapping with previous one, with the biggest coverage
    # while coverage:

    #     # end was reached, finish
    #     if right >= end:
    #         print(s)
    #         break

    #     # choose compatible sprinklers, do not include yourself
    #     compatible = [
    #         [l, r] for l, r in coverage if l <= right and l != left and r != right
    #     ]

    #     # detect gap and finish or proceed
    #     if compatible:
    #         left, right = max(compatible, key=lambda x: x[1])
    #         f = coverage.index([left, right])
    #         coverage = coverage[f:]
    #         s += 1
    #     else:
    #         print("-1")
    #         break

    # trivial case
    if coverage[0][0] <= 0 and coverage[0][1] >= end:
        # print(f"Right side of the grass strip was reached using 1 sprinkler")
        print(1)
        continue

    # parameters
    s = 1
    l_used, r_used = coverage[0]
    l_best, r_best = 0, 0

    for i, (l, r) in enumerate(coverage):
        # first sprinkler can covers the left side of grass strip
        if i == 0 and l > 0:
            # print("Left side of the grass strip can't be covered")
            print(-1)
            break

        # check if last sprinkler can cover the right side of the grass strip
        if i == len(coverage) - 1 and r < end:
            # print("Right side of the grass strip can't be reached")
            print(-1)
            break

        # check if current sprinkler is compatible with previously used sprinkler
        if l <= r_used:
            if r > end:
                # print(
                #     f"Right side of the grass strip was reached using {s + 1} sprinklers"
                # )
                print(s + 1)
                break

            # check if it covers the most area to the right
            if r > r_best:
                # the best from compatible sprinklers
                l_best, r_best = l, r

        # current sprinkler uncompatible with previously used spinkler
        else:
            # check if current sprinkler is compatible with the best sprinkler
            if l <= r_best:
                # best sprinkler gets included in the solution
                s += 1
                l_used, r_used = l_best, r_best

                # current sprinkler becomes the new best
                l_best, r_best = l, r

            # unbreachable gap between sprinklers
            else:
                # print("Unbreachable gap between sprinklers")
                print(-1)
                break

    # loop
    # check if first sprinkler can cover the left side of the strip,
    # no - abort
    # yes - continue

    # check if that sprinkler covers the right side of the strip
    # yes - finish and output number of sprinklers
    # no - continue

    # check if that sprinkler is compatible with the previous one
    # yes - check if it covers the most area to the right
    # yes - store information about that sprinkler
    # no - check if it is compatible with the best sprinkler
    # yes - additional sprinkler needed
    # no - gap between sprinklers, abort
