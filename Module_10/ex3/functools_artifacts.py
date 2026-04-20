from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operators = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operators:
        raise ValueError("Unknow operation")

    return reduce(operators[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="fire")
    water = partial(base_enchantment, power=50, element="water")
    wind = partial(base_enchantment, power=50, element="wind")
    return {
        "fire": fire,
        "water": water,
        "wind": wind
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> Any:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} use {element}, ({power} power)"


if __name__ == "__main__":
    spell_powers = [10, 20, 30, 40]

    print("\nTesting spell reducer...")
    spell_sum = spell_reducer(spell_powers, 'add')
    spell_max = spell_reducer(spell_powers, 'max')
    spell_mult = spell_reducer(spell_powers, 'multiply')
    print(f"Sum: {spell_sum}")
    print(f"Product: {spell_mult}")
    print(f"Max: {spell_max}")

    print("\nTesting partial enchanter...")
    functs = partial_enchanter(base_enchantment)
    print(functs['fire'](target="Dragon"))
    print(functs['water'](target="Well"))
    print(functs['wind'](target="Egle"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher('Fireball'))
    print(dispatcher(['fireball', 'heal', 'shield']))
    print(dispatcher(33.3))
