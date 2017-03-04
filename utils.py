def _is_multiple_of_any(x, numbers):
    return any((x % number == 0 for number in numbers))


def multiples(limit, *numbers):
    return filter(lambda x: _is_multiple_of_any(x, numbers), range(1, limit))


def fibonacci_gen(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True


def factorize(number):
    factors = []
    while number != 1:
        for i in range(2, number+1):
            if number % i == 0:
                factors.append(i)
                number = int(number/i)
                break
    return factors


def is_palindrome(value):
    return str(value) == str(value)[::-1]
