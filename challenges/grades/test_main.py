from main import calculate_average, calculate_concept

print("TESTING calculate_average")
assert calculate_average(10, 10) == 10
assert calculate_average(10, 5) == 7.5
assert calculate_average(9, 1) == 5

print("==========================")
print("TESTING calculate_concept")
assert calculate_concept(10) == "A"
assert calculate_concept(9) == "A"
assert calculate_concept(8.9) == "B"
assert calculate_concept(7.5) == "B"
assert calculate_concept(6) == "C"
assert calculate_concept(4) == "D"
assert calculate_concept(5) == "D"
assert calculate_concept(3.9) == "E"
assert calculate_concept(0) == "E"

print("==========================")
print("\nTESTS PASSED!!! :)")