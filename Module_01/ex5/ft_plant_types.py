class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days, ", end=''
            )


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self) -> None:
        super().get_info()
        print(f"{self.color} color")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = int((self.trunk_diameter**2 * 3.14) / 100)
        print(
            f"{self.name} provides {shade} square meters of shade\n"
            )

    def get_info(self) -> None:
        super().get_info()
        print(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        super().get_info()
        print(f"{self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower = Flower('Rose', 25, 30, 'red')
    tree = Tree('Oak', 500, 1825, 50)
    veg = Vegetable('Tomato', 80, 90, 'summer', 'C')

    flower2 = Flower("Sunflower", 80, 45, "yellow")
    tree2 = Tree("Maple", 400, 1500, 40)
    veg2 = Vegetable("Carrot", 30, 70, "autumn", "A")

    flower.get_info()
    flower.bloom()
    tree.get_info()
    tree.produce_shade()
    veg.get_info()
    print(f"{veg.name} is rich in vitamin {veg.nutritional_value}")
