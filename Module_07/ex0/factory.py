from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling('Flameling', 'Fire')

    def create_evolved(self) -> Pyrodon:
        return Pyrodon('Pyrodon', 'Fire/Flying')


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub('Aquabub', 'Water')

    def create_evolved(self) -> Torragon:
        return Torragon('Torragon', 'Water')
