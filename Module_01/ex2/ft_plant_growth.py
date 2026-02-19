class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth = 0

    def grow(self) -> None:
        self.height += 1
        self.growth += 1

    def age(self) -> None:
        self._age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    plant = Plant('Rose', 25, 30)
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.get_info()
        plant.grow()
        plant.age()
    print(f"Growth this week: +{plant.growth - 1}cm")
