import math


def calc_distance(position: tuple[float, float, float],
                  origin: tuple[float, float, float]) -> None:
    x0, y0, z0 = origin
    x, y, z = position

    distance = math.sqrt((x-x0)**2 + (y-y0)**2 + (z-z0)**2)
    print(f'Distance between {origin} and {position}: {distance:.2f}\n')


if __name__ == "__main__":
    print('=== Game Coordinate System ===\n')
    origin = (0, 0, 0)

    position = (10, 20, 5)
    print(f'Position created: {position}')
    try:
        calc_distance(position, origin)
    except Exception as e:
        print(e)

    print('Parsing coordinates: "3,4,0"')
    coords = "3,4,0"
    parsed_pos = None
    try:
        x, y, z = coords.split(',')
        x, y, z = (int(x), int(y), int(z))
        parsed_pos = (x, y, z)
        print(f'Parsed position: {parsed_pos}')
        calc_distance(parsed_pos, origin)
    except Exception as e:
        print(f'Error parsing coordinates: {e}')

    print('\nParsing invalid coordinates: "abc,def,ghi"')
    coords = "abc,def,ghi"
    try:
        x, y, z = coords.split(',')
        x, y, z = (int(x), int(y), int(z))
    except Exception as e:
        message, = e.args
        print(f'Error parsing coords: {e}')
        print(
            f'Error details - Type: {type(e).__name__}, Args: ("{message}",)')
        print(type(e))

    if parsed_pos:
        print('\nUnpacking demonstration:')
        x, y, z = parsed_pos
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
