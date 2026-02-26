class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def custom_plant_errors(name: str, temp: int) -> None:
    plants = ['carrot', 'tomato', 'potato', 'rose', 'sunflower']
    if name not in plants:
        raise PlantError('Invalid plant name!')
    if temp > 40:
        raise PlantError(f"the {name} plant is wilting!")
    if temp < 0:
        raise PlantError(f"Temperature for {name} is too low!")


def custom_water_errors(tank_level: int):
    if tank_level < 0:
        raise WaterError("Invalid input tank level can't be negative")
    if tank_level < 40:
        raise WaterError('Not enough water in the tank!')


def test_custom_errors():
    print('Testing PlantError...')
    try:
        custom_plant_errors('carrot', -70)
    except PlantError as e:
        print(f'{e}\n')
    except Exception as e:
        print(e)

    print('Testing WaterError...')
    try:
        custom_water_errors(20)
    except WaterError as e:
        print(f'{e}\n')
    except Exception as e:
        print(e)

    print('Testing catching all garden errors...')
    try:
        custom_plant_errors('tomato', 80)
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    except Exception as e:
        print(e)

    try:
        custom_water_errors(30)
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    except Exception as e:
        print(e)

    print('\nAll custom error types work correctly!')


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors()
