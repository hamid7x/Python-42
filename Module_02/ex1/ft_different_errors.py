def garden_operations(err_type: str) -> None:
    if err_type == 'value':
        int('abc')
    elif err_type == 'zero':
        print(7/0)
    elif err_type == 'file':
        f = open('missing.txt')
        f.close()
    elif err_type == 'key':
        plants = {'rose': 'red'}
        print(plants['missing_plant'])


def test_error_types() -> None:
    print('Testing ValueError...')
    try:
        garden_operations('value')
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    except Exception as e:
        print(e)

    print('Testing ZeroDivisionError...')
    try:
        garden_operations('zero')
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    except Exception as e:
        print(e)

    print('Testing FileNotFoundError...')
    try:
        garden_operations('file')
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'\n")
    except Exception as e:
        print(e)

    print('Testing KeyError...')
    try:
        garden_operations('key')
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    except Exception as e:
        print(e)

    print('Testing multiple errors together...')
    try:
        garden_operations('key')
    except (ValueError, ZeroDivisionError, KeyError):
        print('Caught an error, but program continues!\n')
    except Exception as e:
        print(e)
    print('All error types tested successfully!')


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
