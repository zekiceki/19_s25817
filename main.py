from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("Start of the range must be less than the end.")
        else:
            return [x ** 2 for x in range(start, end + 1)]

    def generate_cubes(self, start, end):
        return [x ** 3 for x in range(start, end + 1)]


cubic_gen = CubicGenerator()

start = 1
end = 10

try:
    squares = cubic_gen.generate_squares(start, end)
    print(f"List of squares of numbers from {start} to {end}:")
    print(squares)

    cubes = cubic_gen.generate_cubes(start, end)
    print(f"List of cubes of numbers from {start} to {end}:")
    print(cubes)

except ValueError as e:
    print(e)
