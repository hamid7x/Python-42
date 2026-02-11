def main():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

    plants_data = [
        {'name': 'Rose', 'height': 25, 'age': 30},
        {'name': 'Sunflower', 'height': 80, 'age': 45},
        {'name': 'Cactus', 'height': 15, 'age': 120}
    ]

    for i in range(3):
        name = plants_data[i]['name']
        height = plants_data[i]['height']
        age = plants_data[i]['age']
        print(f"{name}: {height}cm, {age} days old")


if __name__ == "__main__":
    print('=== Garden Plant Registry ===')
    main()