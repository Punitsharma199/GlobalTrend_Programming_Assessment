import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

# Example usage
@measure_execution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
    return tot

# Call the decorated function
result = calculate_multiply([1, 2, 3, 4, 5])
print("Result:", result)

# Function calculate_multiply took 0.0000 seconds to execute
# Result: 120
