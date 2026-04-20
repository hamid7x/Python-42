from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal {target} 'restores {power} power HP'"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} '{power} power HP damage'"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_speels(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_speels


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mega_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return mega_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_spells(target: str, power: int) -> list[str]:
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return cast_spells


if __name__ == "__main__":
    test_values = [19, 22, 20]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined('Dragon', 19)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    power = 10
    multiplier = 3
    mega_spell = power_amplifier(fireball, multiplier)
    result = mega_spell('Wizard', power)
    print(result)
    print(f"Original: {power}, Amplified: {power * multiplier}")

    print("\nTesting condition cast...")
    new_spell = conditional_caster(
        lambda target, power: target == 'Dragon' and power > 15,
        heal
    )
    result = new_spell('Dragon', 20)
    print(result)

    print("\nTesting spell sequence...")
    spells_list = [fireball, heal]
    spells = spell_sequence(spells_list)
    result = spells('Goblin', 30)
    for spell in result:
        print(spell)
