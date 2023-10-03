import math


# solution for first and second problem
def calculate_average_velocity(n, m, v1, v2, v3, T):
    displacement = (1 / n) * v1 * (T / n) + (1 / m) * v2 * (T / m) + (1 - (1 / n) - (1 / m)) * v3 * T
    average_velocity = displacement / T
    return average_velocity


# solution for third problem
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b ** 2 - 4 * a * c

# Check the discriminant to determine the nature of roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2 * a)
    print(f"Root: {root}")
else:
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
