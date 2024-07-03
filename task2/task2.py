#!/usr/bin/env python3

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <file_circle> <file_dot>" % os.path.basename(sys.argv[0]))
        sys.exit(0)

    file_circle = sys.argv[1]
    file_dot = sys.argv[2]

    dots = []

    try:
        with open(file_circle) as f:
            x_circle, y_circle = map(float, f.readline().split())
            r_circle = float(f.readline())

        with open(file_dot) as f:
            for line in f:
                line_dot = line.split()
                dots.append(tuple(map(float, line_dot)))
    except FileNotFoundError as e:
        print(e)
        sys.exit(0)

    r_sqr = r_circle ** 2
    for dot in dots:
        distance = (dot[0] - x_circle) ** 2 + (dot[1] - y_circle) ** 2
        if distance == r_sqr:
            print(0)
        elif distance < r_sqr:
            print(1)
        else:
            print(2)
