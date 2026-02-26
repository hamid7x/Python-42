def water_plants(plant_list: list[str]) -> None:
    print('Opening watering system')
    valid = False
    try:
        for plant in plant_list:
            if not plant or plant.__class__.__name__ != 'str':
                raise ValueError(
                     f'Error: Cannot water {plant} - invalid plant!')
            print(f"Watering {plant}")
        valid = True
    except ValueError as e:
        print(e)
    finally:
        print('Closing watering system (cleanup)')
    if valid:
        print('Watering completed successfully!')


def test_watering_system():
    try:
        print("Testing normal watering...")
        water_plants(['tomato', 'lettuce', 'carrot'])

        print()

        print("Testing with error...")
        water_plants(['tomato', None, 'carrots'])
    except Exception as e:
        print(e)
    finally:
        print('\ncleanup always happens, even with errors!')


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
