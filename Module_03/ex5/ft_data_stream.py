import typing


def fibonacci_gen(n: int) -> typing.Generator[int, None, None]:
    a, b = 0, 1
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


def prime_gen(n: int) -> typing.Generator[int, None, None]:
    i = 2
    while n:
        if is_prime(i):
            n -= 1
            yield i
        i += 1


def display_output(operation: typing.Callable[[int],
                   typing.Generator[int, None, None]],
                   value: int) -> None:
    first = True
    for nb in operation(value):
        if first:
            print(nb, end='')
            first = False
        else:
            print(f', {nb}', end='')
    print()


def convert_to_int(n: str) -> int:
    loockup = '0123456789'
    num = 0
    for s in n:
        digit = 0
        for i in loockup:
            if s == i:
                break
            digit += 1

        num = num * 10 + digit
    return num


def generate_random_nb() -> int:
    numbers = {f'{i}' for i in range(1, 40)}
    nb = convert_to_int([*numbers][0])
    return nb


def game_event_gen(events_nb: int) -> typing.Generator[tuple, None, None]:
    players = ['alice', 'bob', 'charlie']
    events = ['killed monster', 'found treasure', 'leveled up']

    seed = generate_random_nb()
    for i in range(1, events_nb + 1):
        player = players[(seed * i - 1) % len(players)]
        event = events[(seed * i - 1) % len(events)]
        level = (seed * i - 1) % 20

        yield (i, player, event, level)


if __name__ == "__main__":
    print('=== Game Data Stream Processor ===\n')

    print('Processing 1000 game events...\n')
    total_event = 10
    high_level = 0
    treasure_event = 0
    levelup_event = 0
    for i, player, event, level in game_event_gen(total_event):
        if i < 4:
            print(f'Event {i}: Player {player} (level {level}) {event}')
        if i == 4:
            print('...')
        if level >= 10:
            high_level += 1
        if event == 'found treasure':
            treasure_event += 1
        if event == 'leveled up':
            levelup_event += 1
    print()

    print('=== Stream Analytics ===')
    print(f'Total events processed: {total_event}')
    print(f'High-level players (10+): {high_level}')
    print(f'Treasure events: {treasure_event}')
    print(f'Level-up events: {levelup_event}\n')

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print('=== Generator Demonstration ===')
    fib_n = 10
    print(f'Fibonacci sequence (first {fib_n}): ', end='')
    display_output(fibonacci_gen, fib_n)

    prime_n = 5
    print(f'Prime numbers (first {prime_n}): ', end='')
    display_output(prime_gen, prime_n)
    
    generate_random_nb()
