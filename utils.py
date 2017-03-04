def _is_multiple_of_any(x, numbers):
    return any((x % number == 0 for number in numbers))


def multiples(limit, *numbers):
    return filter(lambda x: _is_multiple_of_any(x, numbers), range(1, limit))


def fibonacci_gen(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b
