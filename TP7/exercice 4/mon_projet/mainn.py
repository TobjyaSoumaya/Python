# main.py
from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, to_uppercase

def main():
    # Test des opérations mathématiques
    print(f"Addition de 3 et 2: {add(3, 2)}")
    print(f"Soustraction de 5 et 3: {subtract(5, 3)}")
    print(f"Multiplication de 4 et 5: {multiply(4, 5)}")
    print(f"Division de 10 et 2: {divide(10, 2)}")
    
    # Test des opérations sur les chaînes
    print(f"Concaténation de 'Hello' et ' World': {concatenate('Hello', ' World')}")
    print(f"Majuscule de 'hello': {to_uppercase('hello')}")

if __name__ == "__main__":
    main()
