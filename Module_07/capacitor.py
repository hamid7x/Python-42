from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print(" base:")
    factory = HealingCreatureFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform() -> None:
    print(" base:")
    factory = TransformCreatureFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    test_healing()

    print("\nTesting Creature with transform capaility")
    test_transform()
