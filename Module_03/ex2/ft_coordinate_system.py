import math

if __name__ == "__main__":
    print('=== Game Coordinate System ===\n')
    position = (10, 20, 5)
    x0, y0, z0 = (0, 0, 0)

    print(f'Position created: {position}')
    x1, y1, z1 = position
    distance = math.sqrt((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2)
    print(f'Distance between {x0, y0, z0} and {position}: {distance:.2f}\n')

    print('Parsing coordinates: "3,4,0"')
    coords = "3,4,0"
    try:
        x2, y2, z2 = coords.split(',')
        x2, y2, z2 = (int(x2), int(y2), int(z2))
        parsed_pos = (x2, y2, z2)
        print(f'Parsed position: {parsed_pos}')
        distance = math.sqrt((x2-x0)**2 + (y2-y0)**2 + (z2-z0)**2)
        print(
            f'Distance between {x0, y0, z0} and {parsed_pos}: {distance:.1f}')
    except Exception as e:
        print(f'Error parsing coordinates: {e}')

    print('\nParsing invalid coordinates: "abc,def,ghi"')
    coords = "abc,def,ghi"
    try:
        x3, y3, z3 = coords.split(',')
        x3, y3, z3 = (int(x3), int(y3), int(z3))
    except Exception as e:
        (message, ) = e.args
        print(f'Error parsing coords: {e}')
        print(
            f'Error details - Type: {type(e).__name__}, Args: ("{message}",)')

    print('\nUnpacking demonstration:')
    x, y, z = parsed_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
