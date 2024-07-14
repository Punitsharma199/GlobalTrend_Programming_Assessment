# divide number
try:
    a=int(input("Enter first number :"))
    b=int(input("Enter second number:"))
    c=a/b
    print("The result is :",c)
except ZeroDivisionError:
    print("Do Not enter second number zero")
except ValueError:
    print("system not responding")
print("success")

'''
output:
Enter first number :40
Enter second number:0
Do Not enter second number zero
success
'''