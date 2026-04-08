from abc import ABC, abstractmethod
from ex1.capability import HealCapability, TransformCapability
from ex0.creature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, _) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, (TransformCapability))

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            if isinstance(creature, TransformCapability):
                print(creature.transform())
                print(creature.attack())
                print(creature.revert())
        else:
            raise TypeError("Battle error, aborting tournament: "
                            f"Invalid Creature '{creature.name}' "
                            f"for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            if isinstance(creature, HealCapability):
                print(creature.attack())
                print(creature.heal())
        else:
            raise TypeError("Battle error, aborting tournament: "
                            f"Invalid Creature '{creature.name}' "
                            f"for this defensive strategy")
