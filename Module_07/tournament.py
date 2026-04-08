from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy


def battle(opponemts: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponemts)):
        for j in range(i + 1, len(opponemts)):
            print("* Battle *")
            factory_1, strategy_1 = opponemts[i]
            opp_1 = factory_1.create_base()
            print(opp_1.describe())
            print(" vs")
            factory_2, strategy_2 = opponemts[j]
            opp_2 = factory_2.create_base()
            print(opp_2.describe())
            print(' now fight!')
            try:
                strategy_1.act(opp_1)
                strategy_2.act(opp_2)
            except TypeError as e:
                print(e)
            print()


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved\n")
    battle([(flame_factory, normal), (heal_factory, defensive)])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved\n")
    battle([(flame_factory, aggressive), (heal_factory, defensive)])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved\n")
    battle([(aqua_factory, normal), (heal_factory, defensive),
            (transform_factory, aggressive)])
