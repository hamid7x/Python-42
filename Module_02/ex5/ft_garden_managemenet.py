class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water_level = water
        self.sun_hours = sun


class GardenManager:
    def __init__(self) -> None:
        self.plants = []
        self.water_tank = 10

    def add_plant(self, name: str, water: str, sun: str) -> None:
        if not name:
            raise PlantError('Error adding plant: Plant name cannot be empty!')
        plant = Plant(name, int(water), int(sun))
        self.plants += [plant]
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        if self.water_tank <= 0:
            raise WaterError('Not enough water in tank')

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
                sun_hours: int) -> str:
        if water_level > 10:
            raise WaterError(f'Water level {water_level} is too high (max 10)')
        if water_level < 1:
            raise WaterError(f'Water level {water_level} is too low (min 1)')
        if sun_hours > 12:
            raise PlantError(
                f'sunlight hours {sun_hours} is too high (max 12)')
        if sun_hours < 0:
            raise PlantError(f'sunlight hours {sun_hours} is too low (min 0)')

        return (
             f'{plant_name}: healthy '
             f'(water: {water_level}, sun: {sun_hours})')


def test_garden_management() -> None:
    print('Adding plants to garden...')
    plants_to_add = [
        ('tomato', '5', '8'),
        ('lettuce', '15', '7'),
        ('', '9', '11')
    ]
    m = GardenManager()
    for name, water, sun in plants_to_add:
        try:
            m.add_plant(name, water, sun)
        except PlantError as e:
            print(e)
        except Exception as e:
            print(e)

    print('\nWatering plants...')
    m.water_plants()

    print('\nChecking plant health...')
    for p in m.plants:
        try:
            message = m.check_plant_health(p.name, p.water_level, p.sun_hours)
            print(message)
        except PlantError as e:
            print(f'Error checking {p.name}: {e}')
        except WaterError as e:
            print(f'Error checking {p.name}: {e}')

    print('\nTesting error recovery...')
    try:
        m.water_tank = 0
        m.water_plants()
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    print('System recovered and continuing...\n')

    print('Garden management system test complete!')


if __name__ == "__main__":
    print('=== Garden Management System ===\n')
    test_garden_management()
