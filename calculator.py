def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
num1=float(input("Enter your first number:"))
operator=input("Enter operator")
num2=float(input ("Enter your second number:"))
if operator=="+":
    result=add(num1,num2)
elif operator=="-":
    result=sub(num1,num2)
elif operator=="*":
    result=mul(num1,num2)
else:
    result=divide(num1,num2)
print(result)