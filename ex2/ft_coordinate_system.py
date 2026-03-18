from math import sqrt


def tuple_parser(tuples) -> bool:
    try:
        for x in tuples:
            int(x)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}'")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return False
    return True


def dist(p1, p2):
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def calculate_coordinates():
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    position = (10, 20, 0)

    if tuple_parser(origin) and tuple_parser(position):
        distance = dist(origin, position)
        print(f"\nPosition Created: {position}")
        print(
            f"The distance between {origin} and "
            f"{position}: {distance:.2f}"
        )

    position = (3, 4, 0)
    (x, y, z) = position
    print(f'\nParsing Coordinates "{x},{y},{z}"')

    if tuple_parser(position):
        distance = dist(origin, position)
        print(f"Parsed Position: {position}")
        print(
            f"The distance between {origin} and "
            f"{position}: {distance:.2f}"
        )

    invalid_pos = ("abc", "def", "ghi")
    (a, b, c) = invalid_pos
    print(f'\nParsing invalid coordinates: "{a}","{b}","{c}"')
    tuple_parser(invalid_pos)

    print("\nUnpacking Demonstration")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    calculate_coordinates()
