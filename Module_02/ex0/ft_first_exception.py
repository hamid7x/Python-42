def check_temprature(temp_str: str) -> None:
    try:
        temp_int = int(temp_str)
        if temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        elif temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    except Exception as e:
        print(f"Error: {e}")


def test_temperature_input(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    check_temprature(temp_str)
    print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input('25')
    test_temperature_input('abc')
    test_temperature_input('100')
    test_temperature_input('-5')
    print("All tests completed - program didn't crash!")
