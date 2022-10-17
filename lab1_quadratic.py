import math


def calculate_roots(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    r1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return r1, r2


if __name__ == '__main__':
    coeffs = input("a, b, c: ")
    a, b, c = coeffs.split(', ')

    root1, root2 = calculate_roots(a, b, c)

    print(f"Roots: {root1}, {root2}")
