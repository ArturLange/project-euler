#!/usr/bin/env python3

from utils import fibonacci_gen


def sum_even_fibonacci(limit):
    return sum((x for x in fibonacci_gen(limit) if x % 2 == 0))

if __name__ == '__main__':
    print(sum_even_fibonacci(4000000))
