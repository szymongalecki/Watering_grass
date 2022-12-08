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
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

while True:
    try:
        n, l, w = [int(_) for _ in input().split()]
        print(n, l, w)
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

    # left or right side of the strip are unreachable by sprinklers
    if coverage[0][0] > 0 or coverage[-1][1] < l:
        print("-1")
        break

    # sketch grass strip
    fig, ax = plt.subplots()
    ax.plot()
    ax.add_patch(
        Rectangle((0, 0), l, w, fill=False, color="green", alpha=0.5, linewidth=2)
    )

    # start with no sprinklers, on the left side of the strip
    s = 0
    right = 0

    # choose the sprinkler overlapping with previous one, with the biggest coverage
    while True:
        compatible = [[l, r] for l, r in coverage if l <= right]
        left, right = compatible[-1]

        x = round((left + right) / 2)
        r = sprinkler[x]
        print(f"x: {x}, r: {r}")

        ax.plot(x, w / 2, "bx")
        plt.annotate(f" ({x}, {r})", (x, w / 2))
        ax.add_patch(Circle((x, w / 2), r, alpha=0.3, facecolor="blue"))
        s += 1
        if right >= l:
            print(s)
            plt.title(f"{l} x {w} strip needs {s} sprinklers")
            plt.show()
            break
