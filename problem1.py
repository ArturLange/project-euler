#!/usr/bin/env python3

from utils import multiples


def sum_multiples(limit, *numbers):
    return sum(multiples(limit, *numbers))

if __name__ == '__main__':
    print(sum_multiples(1000, 3, 5))



