#!/usr/bin/env python3

from utils import factorize


def largest_factor(number):
    return factorize(number)[-1]

if __name__ == '__main__':
    print(largest_factor(600851475143))
