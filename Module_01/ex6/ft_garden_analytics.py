class GardenManager:
    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden) -> None:
        self.gardens.append(garden)

    def add_plant(self, garden, plant) -> None:
        garden.plants.append(plant)
        print(f"Added {plant.name} to {garden.owner}'s garden")

    def grow_all(self, garden) -> None:
        print(f"{garden.owner} is helping all plants grow...")
        for p in garden.plants:
            p.grow()
        print()

    def generate_report(self, garden) -> None:
        print(f"=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in garden.plants:
            print(f"- {p.get_info()}")
        print()

    def get_scores(self) -> None:
        print("Garden scores - ", end='')
        i = len(self.gardens)
        for g in self.gardens:
            score = 0
            i -= 1
            for p in g.plants:
                score += p.height
            print(f"{g.owner}: {score}", end='')
            if i > 0:
                print(", ", end='')
        print()

    def total_garden(self) -> int:
        return len(self.gardens)

    @classmethod
    def create_garden_network(cls, data):
        manager = GardenManager()
        for d in data:
            new_garden = Garden(d)
            manager.add_garden(new_garden)
        return manager

    @staticmethod
    def validate_height(garden) -> bool:
        for p in garden.plants:
            if p.height < 0:
                return False
        return True

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def get_stats(self) -> None:
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
                  f"Plant types: {regular} regular, "
                  f"{flowering} flowering, {prize} prize flowers"
                  )
            print()


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self) -> None:
        self.height += 1
        self.growth += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_category(self) -> str:
        return "plant"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
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

    def get_info(self) -> str:
        parent_info = super().get_info()
        return f"{parent_info}, Prize points: {self.prize_point}"

    def get_category(self) -> str:
        return "prize"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===", end='\n\n')
    p = Plant('Oak Tree', 101, 30)
    p1 = FloweringPlant('Rose', 26, 50, 'red')
    p2 = PrizeFlower('Sunflower', 51, 20, 'yellow', 10)

    manager = GardenManager()
    alice_garden = Garden('Alice')
    bob_garden = Garden('Bob')

    manager.add_plant(alice_garden, p)
    manager.add_plant(alice_garden, p1)
    manager.add_plant(alice_garden, p2)
    manager.add_plant(bob_garden, p2)
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    print()

    manager.grow_all(alice_garden)
    manager.generate_report(alice_garden)

    alice_stats = GardenManager.GardenStats(alice_garden)
    alice_stats.get_stats()

    validation = GardenManager.validate_height(alice_garden)
    print(f"Hieght validation test: {validation}")
    manager.get_scores()
    print(f"Total gardens managed: {manager.total_garden()}")
