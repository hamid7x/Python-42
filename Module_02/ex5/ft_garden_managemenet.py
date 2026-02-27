class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []
        self.water_tank = 5

    def add_plant(self, name: str, water: str, sun: str) -> None:
        try:
            plant = Plant(name, int(water), int(sun))
            self.plants.append(plant)
            print(f"Added {name} successfully")
        except GardenError as e:
            print(f'Error adding plant: {e}')

    def water_plants(self) -> None:
        if self.water_tank <= 0:
            raise WaterError('Not enough in tank')

        print('Opening watering system')
        try:
            for p in self.plants:
                print(f'Watering {p.name} - success')
        finally:
            print('Closing watering system (cleanup)')

    def check_plant_health(
                self,
                plant_name: str,
                water_level: int,
                sun_hours: int) -> None:
        if water_level > 10:
            raise WaterError(
                f'Error checking {plant_name}: '
                f'Water level {water_level} is too high (max 10)')
        if water_level < 1:
            raise WaterError(
                f'Error checking {plant_name}: '
                f'Water level {water_level} is too low (min 1)'
            )
        if sun_hours > 12:
            raise PlantError(
                f'Error checking {plant_name}: '
                f'sunlight hours {sun_hours} is too high (max 12)'
            )
        print(
             f'{plant_name}: healthy '
             f'(water: {water_level}, sun: {sun_hours})')


class Plant:
    def __init__(self, name: str, water_level: int, sun_hours: int) -> None:
        if not name:
            raise PlantError('Plant name cannot be empty')
        if water_level < 0:
            raise WaterError('Water level cannot be negative')
        if sun_hours < 0:
            raise PlantError('Sunlight hours cannot be negative')
        self.name = name
        self.water_level = water_level
        self.sun_hours = sun_hours


def test_garden_managemenet():
    print('Adding plants to garden...')
    plants_to_add = [
        ('tomato', 'abc', '8'),
        ('lettuce', '15', '7'),
        ('', '9', '11')
    ]
    m = GardenManager()
    for name, water, sun in plants_to_add:
        try:
            m.add_plant(name, water, sun)
        except Exception as e:
            print(e)

    print('\nWatering plants...')
    m.water_plants()

    print('\nChecking plant health...')
    try:
        for p in m.plants:
            try:
                m.check_plant_health(p.name, p.water_level, p.sun_hours)
            except GardenError as e:
                print(e)
    except Exception as e:
        print(e)

    print('\nTesting error recovery...')
    try:
        m.water_tank = 0
        m.water_plants()
    except GardenError as e:
        print(f'caught GardenError: {e}')
    print('System recovered and continuing...\n')

    print('Garden management system test complete!')


if __name__ == "__main__":
    print('=== Garden Management System ===\n')
    test_garden_managemenet()
