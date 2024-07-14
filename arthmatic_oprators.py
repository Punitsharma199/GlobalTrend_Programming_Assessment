def addition(num1, num2):
    a = num1 + num2
    print("addition was performed on the two numbers ", num1, ' and ', num2)
    return a


def subtraction(num1, num2):
    s = num1 - num2
    print("subtraction was performed on the two numbers ", num1, ' and ', num2)
    return s


def multiplication(num1, num2):
    t = num1 * num2
    print("multiplication was performed on the two numbers ", num1, ' and ', num2)
    return t


def division(num1, num2):
    d = num1 / num2
    print("division was performed on the two numbers ", num1, ' and ', num2)
    return d


def calculate(num1, num2, string):
    result = None
    if string == '+':
        result = addition(num1, num2)
    elif string == '-':
        result = subtraction(num1, num2)
    elif string == '*':
        result = multiplication(num1, num2)
    elif string == '/':
        result = division(num1, num2)

print(addition(num1=4,num2=5))
print(subtraction(num1=4,num2=5))
print(multiplication(num1=4,num2=5))
print(division(num1=4,num2=5))

'''
output:

addition was performed on the two numbers  4  and  5
9
subtraction was performed on the two numbers  4  and  5
-1
multiplication was performed on the two numbers  4  and  5
20
division was performed on the two numbers  4  and  5
0.8
'''