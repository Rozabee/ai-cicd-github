"""Simple utility functions - you'll add more!"""


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

if __name__ == "__main__":
    result = multiply(9, 9)
    print("-----------------------------------")
    print(f"The result of 9 multiplied by 9 is: {result}")
    print("-----------------------------------")

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

