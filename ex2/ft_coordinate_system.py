from math import sqrt


def tuple_parser(data: str):
    try:
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("Expected 3 values")
        result = (float(parts[0]), float(parts[1]), float(parts[2]))
        return result
    except ValueError:
        print("Invalid Syntax")
        return


def dist(p1, p2):
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def calculate_coordinates():
    print("=== Game Coordinate System ===")

    origin = (0.0, 0.0, 0.0)
    user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
    position = tuple_parser(user_input)

    if position is not None:
        (x, y, z) = position
        distance = dist(origin, position)
        print(f"\nGot a first tuple: {position}")
        print(f"It includes X={x}, Y={y}, Z={z}")
        print(f"Distance to the center: {distance:.4f}")


if __name__ == "__main__":
    calculate_coordinates()