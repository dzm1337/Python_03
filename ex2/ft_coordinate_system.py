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
		return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def calculate_coordinates():
		print("=== Game Coordinate System ===")
	
		coordinates = (0, 0, 0)
		coordinates2 = (10, 20, 0)
		distance = dist(coordinates, coordinates2)

		if tuple_parser(coordinates) == True and tuple_parser(coordinates2) == True:
			print(f"\nPosition Created: {coordinates2}")
			print(f"The distance between {coordinates} and {coordinates2}: {distance:.2f}")

		coordinates2 = (3, 4, 0)
		(x2, y2, z2) = coordinates2
		print(f'\nParsing Coordinates "{x2},{y2},{z2}"')

		if (tuple_parser(coordinates2) == True):
			print(f"Parsed Position: {coordinates2}")
			print(f"The distance between {coordinates} and {coordinates2}: {distance:.2f}")
		
		coordinates2 = ("abc", "def", "ghi")
		(a, b, c) = coordinates2
		print(f'\nParsing invalid coordinates: "{a}","{b}","{c}"')
		tuple_parser(coordinates2)
		
		print("\nUnpacking Demonstration")
		print(f"Player at x={x2}, y={y2}, z={z2}")
		print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
			
if __name__ == "__main__":
	calculate_coordinates()
