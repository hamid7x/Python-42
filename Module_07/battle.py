from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def testing_battle(factory_1: CreatureFactory,
                   factory_2: CreatureFactory) -> None:
    print("Testing battle")
    base_creature_1 = factory_1.create_base()
    base_creature_2 = factory_2.create_base()
    print(base_creature_1.describe())
    print(' vs.')
    print(base_creature_2.describe())
    print(' fight!')
    print(base_creature_1.attack())
    print(base_creature_2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aquabub_factory = AquaFactory()
    testing_factory(flame_factory)
    testing_factory(aquabub_factory)
    testing_battle(flame_factory, aquabub_factory)
