from typing import Any
from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(item: str) -> str:
        return f"{enchantment_type} {item}"
    return factory


def memory_vault() -> dict[str, Callable]:
    memory_store = {}

    def store(key: Any, value: Any) -> None:
        memory_store.update({key: value})

    def recall(key: Any) -> Any:
        return memory_store.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    init_power = 100
    amount = 20
    accumulator = spell_accumulator(init_power)
    print(f"Base {init_power}, add {amount}: {accumulator(amount)}")
    amount = 30
    print(f"Base {init_power}, add {amount}: {accumulator(amount)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory('Flaming')
    print(flaming('Sword'))
    frozen = enchantment_factory('Frozen')
    print(frozen('Shield'))

    print("\nTesting memory vault...")
    my_memory = memory_vault()
    key = 'secret'
    value = 42
    store = my_memory['store']
    recall = my_memory['recall']

    store(key, value)
    print(f"Store '{key}' = {value}")
    print(f"Recall '{key}': {recall(key)}")
    key = 'unknown'
    print(f"Recal '{key}': {recall(key)}")
