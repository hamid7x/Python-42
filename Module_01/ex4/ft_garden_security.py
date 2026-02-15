
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {name}")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print('Security: Negative height rejected\n')
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print('Security: Negative age rejected\n')
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant('Rose', 3, 10)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    height = plant.get_height()
    age = plant.get_age()
    print(f"Current plant: {plant.name} ({height}cm, {age} days)")
