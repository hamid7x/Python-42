class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}")

    def get_info(self) -> None:
        print(
              f"Current plant: {self.name}"
              f"({self._height}cm, {self._age} days)"
            )

    def invalid_operation(self, op: str, val: int) -> None:
        temp = {'height': 'cm', 'age': ' days'}
        print(f"Invalid operation attempted: {op} {val}{temp[op]} [REJECTED]")
        print(f"Security: Negative {op} rejected")

    def get_height(self) -> int:
        return self._height

    def set_height(self, height: int) -> None:
        if height < 0:
            self.invalid_operation('height', height)
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            self.invalid_operation('age', age)
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant('plant', 20, 15)
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    plant.set_age(-40)
    print()
    plant.get_info()
