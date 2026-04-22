from functools import wraps
from collections.abc import Callable
import time
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            result = "Insufficient power for this spell"
            power = args[-1]
            if power >= min_power:
                result = func(*args)
            return result
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper() -> str:
            for atm in range(max_attempts):
                try:
                    result = func()
                    return result
                except Exception as e:
                    atm += 1
                    if atm != max_attempts:
                        print(
                            f"{e}, retrying... (attempt {atm}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return all(c.isalpha() or c.isspace() for c in name) and len(name) >= 3

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@spell_timer
def heal(target: str, power: int) -> str:
    time.sleep(0.101)
    return f"Heal {target}, restores {power} power"


@power_validator(60)
def cast_spell(power: int) -> str:
    return f"Spell cast! with power {power}"


@retry_spell(max_attempts=3)
def spell() -> str:
    if random.random() < 0.99:
        raise Exception("Spell failed")
    return "Waaaaaaagh spelled !"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    print(f"Result: {cast_spell(100)}")

    print("\nTesting retrying spell...")
    print(f"{spell()}")

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(MageGuild.validate_mage_name('Alex'))
    print(MageGuild.validate_mage_name('Alex23'))
    print(mage.cast_spell('Lightning', 15))
    print(mage.cast_spell('Shadow', 8))
