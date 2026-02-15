
class Plant:
    counter = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.counter += 1
        print(f"Created: {name} ({height}cm, {age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants_data = [
        {'name': 'Rose', 'height': 25, 'age': 30},
        {'name': 'Oak', 'height': 200, 'age': 365},
        {'name': 'Cactus', 'height': 5, 'age': 90},
        {'name': 'Sunflower', 'height': 80, 'age': 45},
        {'name': 'Fern', 'height': 15, 'age': 120}
    ]
    for i in range(5):
        name = plants_data[i]['name']
        height = plants_data[i]['height']
        age = plants_data[i]['age']
        plant = Plant(name, height, age)
    print(f"\nTotal plants created: {Plant.counter}")
