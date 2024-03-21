def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]
start = 1
end = 10
squares = generate_squares(start, end)
print(f"List of squares of numbers from {start} to {end}:")
print(squares)