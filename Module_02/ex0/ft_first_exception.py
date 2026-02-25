def check_temperature(temp_str: str) -> int | None:
    print(f"Testing temperature: {temp_str}")
    try:
        try:
            temp_int = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number")
            return None
        if temp_int > 40:
            raise ValueError(
                            f"Error: {temp_int}°C"
                            f" is too hot for plants (max 40°C)")
        elif temp_int < 0:
            raise ValueError(
                            f"Error: {temp_int}°C"
                            f" is too cold for plants (min 0°C)"
                            )
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
            return temp_int
    except ValueError as err:
        print(err)
        return None


def test_temperature_input() -> None:
    temp_tests = ['25', 'abc', '100', '-50']
    for temp in temp_tests:
        try:
            check_temperature(temp)
        except Exception as e:
            print(e)
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
