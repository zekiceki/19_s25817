class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


square_gen = SquareGenerator()
start = 1
end = 10
squares = square_gen.generate_squares(start, end)
print(f"List of squares of numbers from {start} to {end}:")
print(squares)
