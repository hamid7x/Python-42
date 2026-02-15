class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        self.color = color
        super().__init__(name, height, age)

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age)


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, age)
