
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print('=== Garden Plant Registry ===')
    plants = [
        Plant('Rose', 25, 30),
        Plant('Sunflower', 80, 45),
        Plant('Cactus', 15, 120)
    ]
    for plant in plants:
        name = plant.name
        height = plant.height
        age = plant.age
        print(f"{name}: {height}cm, {age} days old")
