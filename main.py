import math

class Calculator:
    """Simple calculator class."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Raises an exception if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, a):
        """Return the square root of a. Raises an exception if a is negative."""
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)

def main():
    calculator = Calculator()

    # Example calculations
    a, b = 10, 5
    print(f"The sum of {a} and {b} is {calculator.add(a, b)}.")
    print(f"The difference between {a} and {b} is {calculator.subtract(a, b)}.")
    print(f"The product of {a} and {b} is {calculator.multiply(a, b)}.")
    print(f"The division of {a} by {b} is {calculator.divide(a, b)}.")
    print(f"The square root of {a} is {calculator.square_root(a)}.")

if __name__ == "__main__":
    main()

