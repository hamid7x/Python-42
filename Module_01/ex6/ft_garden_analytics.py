class GardenManager:
    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: 'Garden') -> None:
        self.gardens.append(garden)

    def create_garden_network(cls, data: list['Garden']) -> 'GardenManager':
        manager = cls()
        for d in data:
            manager.gardens.append(d)
        return manager
    create_garden_network = classmethod(create_garden_network)

    class GardenStats:
        def __init__(self, garden: 'Garden') -> None:
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

    def total_gardens(gardens: list['Garden']) -> int:
        return len(gardens)
    total_gardens = staticmethod(total_gardens)


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: 'Plant', flag: bool = True) -> None:
        self.plants.append(plant)
        if flag:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
        print()

    def generate_report(self) -> None:
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


def validate_height(garden: 'Garden') -> bool:
    for p in garden.plants:
        if p.height < 0:
            return False
    return True


if __name__ == "__main__":
    print("=== Garden Management System Demo ===", end='\n\n')
    p1 = Plant('Oak Tree', 100, 30)
    p2 = FloweringPlant('Rose', 25, 50, 'red')
    p3 = PrizeFlower('Sunflower', 50, 20, 'yellow', 10)
    p4 = Plant('Maple Tree', 96, 100)

    alice_garden = Garden('Alice')
    bob_garden = Garden('Bob')
    manager = GardenManager.create_garden_network([alice_garden, bob_garden])

    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)
    bob_garden.add_plant(p4, False)

    print()

    alice_garden.grow_all()
    alice_garden.generate_report()

    alice_stats = manager.GardenStats(alice_garden)
    alice_stats.get_stats()

    validation = validate_height(alice_garden)
    print(f"Height validation test: {validation}")
    manager.get_scores()
    total_gardens = GardenManager.total_gardens(manager.gardens)
    print(f"Total gardens managed: {total_gardens}")
