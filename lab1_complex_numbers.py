class ComplexNumber:
    def __init__(self, r, i=0.0):
        self.real = r
        self.imag = i

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"({self.real} + {self.imag}j)"

    def __repr__(self):
        rep = f'ComplexNumber{self.__str__()}'
        return rep

    def print_number(self):
        print(self.__str__())


if __name__ == '__main__':
    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(-1, 4)

    for _ in range(1):
        print(f"Test: {num1} + {num2}")
        num3 = num1 + num2
        print(f"Result: {num3}")

        print(f"Test: {num1} - {num2}")
        num3 = num1 - num2
        print(f"Result: {num3}")

        print(f"Test: {num1} * {num2}")
        num3 = num1 * num2
        print(f"Result: {num3}")
