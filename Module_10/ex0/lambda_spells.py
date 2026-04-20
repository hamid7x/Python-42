def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    sum_power = sum(list(map(lambda m: m['power'], mages)))
    avg_power = round(sum_power / len(mages), 2)

    return {
            "max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Shadow Blade', 'power': 78, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
    ]
    mages = [
        {'name': 'Aldric', 'power': 45, 'element': 'fire'},
        {'name': 'Lyra', 'power': 82, 'element': 'water'},
        {'name': 'Zephyr', 'power': 63, 'element': 'air'},
        {'name': 'Terra', 'power': 91, 'element': 'earth'},
        {'name': 'Nova', 'power': 38, 'element': 'lightning'},
    ]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']}"
          f" ({sorted_artifacts[0]['power']} power)"
          f" comes before {sorted_artifacts[1]['name']}"
          f" ({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 50)
    for mage in filtered_mages:
        print(f"{mage['name']} (power: {mage['power']}) passed the filter")

    print("\nTesting Transform...")
    spells = ['fireball', 'heal', 'shield']
    transformed_spells = spell_transformer(spells)
    for s in transformed_spells:
        print(s, end=' ')

    print("\n\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Averge power: {stats['avg_power']}")
