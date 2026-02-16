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
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    def produce_shade(self):
        shade = (self.trunk_diameter**2 * 3.14) / 100
        print(f"{self.name} provides {int(shade)} square meters of shade\n")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, age)


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Sunflower", 80, 45, "yellow")
    print(
        f"{flower1.name} (Flower): {flower1.height}cm, "
        f"{flower1.age} days, {flower1.color} color"
    )
    flower1.bloom()
    print(
        f"{flower2.name} (Flower): {flower2.height}cm, "
        f"{flower2.age} days, {flower2.color} color"
    )
    flower2.bloom()

    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Maple", 400, 1500, 40)
    print(
        f"{tree1.name} (Tree): {tree1.height}cm, "
        f"{tree1.age} days, {tree1.trunk_diameter}cm diameter"
    )
    tree1.produce_shade()
    print(
        f"{tree2.name} (Tree): {tree2.height}cm, "
        f"{tree2.age} days, {tree2.trunk_diameter}cm diameter"
    )
    tree2.produce_shade()

    veg1 = Vegetable("Tomato", 80, 90, "summer", "C")
    veg2 = Vegetable("Carrot", 30, 70, "autum", "A")
    print(
        f"{veg1.name} (Vegetable): {veg1.height}cm, "
        f"{veg1.age} days, {veg1.harvest_season} harvest"
    )
    print(f"{veg1.name} is rich in vitamin {veg1.nutritional_value}\n")
    print(
        f"{veg2.name} (Vegetable): {veg2.height}cm, "
        f"{veg2.age} days, {veg2.harvest_season} harvest"
    )
    print(f"{veg2.name} is rich in vitamin {veg2.nutritional_value}")
