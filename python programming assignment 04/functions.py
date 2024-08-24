#Pre-defined Function:

result: int = len("Hello, World!")
print(result)  
# Output: 12

#User-defined Function:

def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("Raza")  
# Output: Hello,  Raza!

#Arguments and Parameters

def add(a: int, b: int) -> int:
    return a + b

result: int = add(3, 9)
result1: int = add(5, 5)
print(result)
print(result1)  
# Output: 12
# Output: 10

#Default Functions

def power(base: int, exponent: int = 2) -> int:
    return base ** exponent

print(power(5))        
print(power(2, 2))    
# Output: 25
# Output:4

#Optional, Positional, and Keyword Arguments

def greet(name: str = "Guest") -> None:
    print(f"Hello, {name}!")

            
greet("Ali")      

# Output: Hello, Ali!
# Output: Hello, Guest!

#Positional Arguments

def subtract(a: int, b: int) -> int:
    return a - b

result: int = subtract(50, 25)
print(result)  
# Output: 25

#Keyword Argument:

def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor

result: float = divide(divisor=7, dividend=49)
print(result)  
# Output: 7.00

#Lambda Functino:

square: callable = lambda x: x * x
print(square(6))  
# Output: 36

#Recursive Functions

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result: int = factorial(8)
print(result)  
# Output: 120

#Decorators

def my_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> None:
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

say_hello("aamir")

