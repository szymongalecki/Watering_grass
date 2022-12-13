"""
python3 gen.py | python3 wg.py > res.txt
"""

import random

cases = 10 ** 3

for _ in range(cases):
    n = random.randrange(1, 10 ** 4 + 1)
    l = random.randrange(1, 10 ** 7 + 1)
    w = random.randrange(1, 10 ** 2 + 1)
    print(n, l, w)

    for _ in range(n):
        x = random.randrange(0, l + 1)
        r = random.randrange(1, 10 ** 3 + 1)
        print(x, r)
