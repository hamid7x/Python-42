
class Plant:
    growth = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self._age = age

    def grow(self):
        Plant.growth += 1
        self.height += 1

    def age(self):
        self._age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    my_plant = Plant('Rose', 25, 30)
    for i in range(1, 7):
        print(f"=== Day {i} ===")
        name = my_plant.name
        height = my_plant.height
        age = my_plant._age
        print(f"{name}: {height}cm, {age} days old")
        my_plant.grow()
        my_plant.age()
    print(f'Growth this week: +{Plant.growth}cm')
