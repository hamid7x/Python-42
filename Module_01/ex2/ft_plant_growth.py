class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self._age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    plants = [
        Plant('Rose', 25, 30),
        Plant('Cactus', 5, 90),
        Plant('Sunflower', 80, 45)
    ]
    print("=== Day 1 ===")
    for p in plants:
        p.get_info()
    for i in range(1, 7):
        for p in plants:
            p.grow()
            p.age()
    print(f"=== Day {i + 1} ===")
    for p in plants:
        p.get_info()
    print(f"Growth this week: +{i}cm")
