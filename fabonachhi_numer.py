def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.
    """
    if(n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(fibonacci(10))

# output: 55