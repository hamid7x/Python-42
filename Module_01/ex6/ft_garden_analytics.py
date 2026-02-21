class GardenManager:
    total = 0

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden) -> None:
        self.gardens.append(garden)
        self.total += 1

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def stats(self) -> None:
            total_growth = 0
            regular = 0
            flowering = 0
            prize = 0
            for p in self.garden.plants:
                total_growth += p.growth
                category = p.get_category()
                if category == "plant":
                    regular += 1
                elif category == "flowering":
                    flowering += 1
                elif category == "prize":
                    prize += 1
            print(
                f"Plants added: {len(self.garden.plants)}, "
                f"Total growth: {total_growth}cm"
                )
            print(
                  f"Plants types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers"
                  )


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()

    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.get_info()}")
        print()


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self) -> None:
        self.height += 1
        self.growth += 1
        print(f"{self.name} grow 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_category(self) -> str:
        return "plant"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        parent_info = super().get_info()
        return f"{parent_info}, {self.color} flowers (blooming)"

    def get_category(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str,
            prize_point: int
            ) -> None:
        super().__init__(name, height, age, color)
        self.prize_point = prize_point

    def get_info(self) -> None:
        parent_info = super().get_info()
        return f"{parent_info}, Prize points: {self.prize_point}"

    def get_category(self) -> str:
        return "prize"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    p = Plant('Oak Tree', 101, 30)
    p1 = FloweringPlant('Rose', 26, 50, 'color')
    p3 = FloweringPlant('Cactus', 26, 50, 'green')
    p2 = PrizeFlower('Sunflower', 51, 20, 'yellow', 10)
    print()
    alice_garden = Garden('Alice')
    alice_garden.add_plant(p)
    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)
    print()
    alice_garden.grow_all()
    p1.grow()
    print()
    alice_garden.generate_report()
    bob_garden = Garden('Bob')

    manager = GardenManager()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)
    stats = manager.GardenStats(alice_garden)
    stats.stats()
