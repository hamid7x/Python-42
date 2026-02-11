def main():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self._age = age

        def grow(self):
            self.height += 1
        
        def age(self):
            self._age += 1
        
        def get_info(self):
            print(f"{self.name}: {self.height}cm, {self.age} days old")

    my_plant = Plant('Rose', 25, 30)
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        print(f"{my_plant.name}: {my_plant.height}cm, {my_plant._age} days old")
        my_plant.grow()
        my_plant.age()
    print(f'Growth this week: +{i - 1}cm')


if __name__ == "__main__":
    main()
