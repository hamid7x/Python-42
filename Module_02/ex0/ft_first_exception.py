def check_temperature(temp_str: str) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not valid number")
    if temp_int > 40:
        raise ValueError(
            f"Error: {temp_int}°C is too hot for plants (max 40°C)")
    if temp_int < 0:
        raise ValueError(
            f"Error: {temp_int}°C is too cold for plants (min 0°C)")

    return temp_int


def test_temperature_input() -> None:
    try:
        temp_tests = ['25', 'abc', '100', '-50']
        for temp in temp_tests:
            try:
                value = check_temperature(temp)
                print(f"Temperature {value}°C is perfect for plants!")
            except Exception as e:
                print(e)
            print()
    except Exception as err:
        print(err)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
