# Problem: Factorial of a Number
# 5! = 5x4x3x2x1 = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # recursion!

print(factorial(5))    # 120
print(factorial(0))    # 1
print(factorial(10))   # 3628800