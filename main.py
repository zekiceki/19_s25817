import math

from square_generator.square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):

        return [x ** 3 for x in range(start, end + 1)]

cubic_gen = CubicGenerator()

start = 1
end = 10

cubes = cubic_gen.generate_cubes(start, end)

cube_roots = [math.pow(x, 1/3) for x in cubes]

print(f"List of cubes of numbers from {start} to {end}:")
print(cubes)

print("Cube roots of the numbers:")
print(cube_roots)