def fib(x):
    if x == 1 or x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)

# Simple example of recursion
print(fib(3))
print(fib(6))