for value in range(1, 21, 2):
  print(value)

mill_range_val = list(range(1, 1000001))

print(min(mill_range_val))
print(max(mill_range_val))
# print(sum(value))

# multiples of three
for multiple_three in range(1, 11):
  result = multiple_three * 3
  print(f'3x{multiple_three} = {result}')

# cubes
cubes = []
for cube_val in range(1, 11):
  cube = cube_val**3
  print(cube)

# list comprehension cubes
cubes2 = [cube2_val**3 for cube2_val in range(1, 11)]
print(cubes2)
