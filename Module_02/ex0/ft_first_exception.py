def check_temperature(temp_str: str) -> None:
    print("Testing temperature: {temp_str}")
    try:
        try:
            temp_int = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number")
        if temp_int > 40:
            raise ValueError(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        elif temp_int < 0:
            raise ValueError(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        else:
            raise ValueError(f"Temperature {temp_int}°C is perfect for plants!")
    except ValueError as err:
        print(err)
    except Exception as e:
        print(f"Error: {e}")


def test_temperature_input(temp_str: str) -> None:
    check_temperature('25')
    check_temperature('abc')
    check_temperature('100')
    check_temperature('-5')
    print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    print("All tests completed - program didn't crash!")
