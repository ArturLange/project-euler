#!/usr/bin/env python3

from utils import generate_primes


def get_nth_prime(n):
    return tuple(generate_primes(n))[-1]


if __name__ == '__main__':
    print(get_nth_prime(10001))
