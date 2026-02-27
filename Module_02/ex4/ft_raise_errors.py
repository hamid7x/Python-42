def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError('Error: Plant name cannot be empty!\n')
    if water_level > 10:
        raise ValueError(
            f'Error: Water level {water_level} is too high (max 10)\n')
    if water_level < 1:
        raise ValueError(
            f'Error: water level {water_level} is too low (min 1)\n')
    if sunlight_hours > 12:
        raise ValueError(
            f'Error: Sunlight hours {sunlight_hours} is too high (max 12)\n')
    if sunlight_hours < 2:
        raise ValueError(
            f'Error: Sunlight hours {sunlight_hours} is too low (min 2)\n')

    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    print('Testing good values...')
    try:
        check_plant_health('tomato', 5, 7)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

    print('Testing empty plant name...')
    try:
        check_plant_health('', 4, 6)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

    print('Testing bad water level...')
    try:
        check_plant_health('tomato', 15, 8)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

    print('Testing bad sunlight hours...')
    try:
        print(check_plant_health('tomato', 6, 0))
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

    print('All error raising tests completed!')


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
