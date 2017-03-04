#!/usr/bin/env python3

from utils import is_palindrome


def products():
    for i in range(100,1000):
        for j in range(i, 1000):
            yield i * j


def largest_palindrome_product():
    palindromes = (x for x in products() if is_palindrome(x))
    largest = 0
    for product in palindromes:
        if product > largest:
            largest = product
    return largest


if __name__ == '__main__':
    print(largest_palindrome_product())
