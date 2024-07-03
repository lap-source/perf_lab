#!/usr/bin/env python3

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <n> <m>" % os.path.basename(sys.argv[0]))
        sys.exit(0)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Error: invalid argument")
        sys.exit(1)

    path_found = []

    for i in range(n):
        p = 1 + (i * (m - 1)) % n
        if p == 1 and i != 0:
            break
        path_found.append(str(p))
    print(''.join(path_found))
