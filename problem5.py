#!/usr/bin/env python3

from utils import lcm
from functools import reduce


def largest_multiple(numbers):
    return reduce(lambda a, b: lcm(a, b), numbers)


if __name__ == '__main__':
    print(largest_multiple(range(1, 21)))
