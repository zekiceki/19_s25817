import math

class SquareGenerator:
    def generate_squares(self, start, end):

        return [x ** 2 for x in range(start, end + 1)]

square_gen = SquareGenerator()

start = 1
end = 10

squares = square_gen.generate_squares(start, end)

square_roots = [math.sqrt(x) for x in squares]
print(f"List of squares of numbers from {start} to {end}:")
print(squares)
print("Square roots of the numbers:")
print(square_roots)
