def fibonacci(n: int) -> None:
    a = 0
    b = 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime(n: int):
    i = 2
    while n:
        if is_prime(i):
            n -= 1
            yield i
        i += 1


def display_output(operation, value: int) -> None:
    first = True
    for nb in operation(value):
        if first:
            print(nb, end='')
            first = False
        else:
            print(f', {nb}', end='')
    print()


if __name__ == "__main__":
    print('=== Game Data Stream Processor ===\n')
    print('Processing 1000 game events...')

    fib_n = 10
    print(f'Fibonacci sequence (first {fib_n}): ', end='')
    display_output(fibonacci, fib_n)

    prime_n = 5
    print(f'Prime numbers (first {prime_n}): ', end='')
    display_output(prime, prime_n)
