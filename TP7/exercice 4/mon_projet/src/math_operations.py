# src/math_operations.py

def add(a, b):
    """Additionne deux nombres."""
    return a + b

def subtract(a, b):
    """Soustrait deux nombres."""
    return a - b

def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b

def divide(a, b):
    """Divise deux nombres, en gérant la division par zéro."""
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b
