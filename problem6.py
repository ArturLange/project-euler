#!/usr/bin/env python3


def sum_of_squares(sequence):
    return sum((x**2 for x in sequence))


def square_of_sums(sequence):
    return sum(sequence) ** 2


def difference(limit):
    return square_of_sums(range(limit+1)) - sum_of_squares(range(limit+1))


if __name__ == '__main__':
    print(difference(100))
