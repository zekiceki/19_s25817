import math

from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()


start = 1
end = 10

try:

    squares = square_gen.generate_squares(start, end)

    square_roots = [math.sqrt(x) for x in squares]

    print(f"List of squares of numbers from {start} to {end}:")
    print(squares)
    print("Square roots of the numbers:")
    print(square_roots)

except ValueError as e:
    print(f"Error: {e}")
