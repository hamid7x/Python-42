class GardenError(Exception):
    def __init__(self, message: str = 'Garden Error!') -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = 'Plant Error!') -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = 'Water Error!') -> None:
        super().__init__(message)


def custom_plant_errors(name: str) -> None:
    if name:
        raise PlantError(f"The {name} plant is wilting!")


def custom_water_errors(tank_level: int) -> None:
    if tank_level <= 0:
        raise WaterError('Not enough water in the tank!')


def test_custom_errors() -> None:
    print('Testing PlantError...')
    try:
        custom_plant_errors('tomato')
    except PlantError as e:
        print(f'Caught PlantError: {e}\n')
    except Exception as e:
        print(e)

    print('Testing WaterError...')
    try:
        custom_water_errors(-2)
    except WaterError as e:
        print(f'Caught WaterError: {e}\n')
    except Exception as e:
        print(e)

    print('Testing catching all garden errors...')
    try:
        custom_plant_errors('tomato')
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    except Exception as e:
        print(e)

    try:
        custom_water_errors(0)
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    except Exception as e:
        print(e)

    print('\nAll custom error types work correctly!')


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors()
