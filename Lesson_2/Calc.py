num_1 = input("Enter the number1: ")
oper = input("Enter the operator: ")
num_2 = input("Enter the number2: ")

def num(a):
    try:
        a = float(a)
        return a
    except Exception as x:
        print("Hey man, do you think it`s funny ? this is not a number")
        a = input("Enter the number1: ")
        exit()

def calculation(operator,n1,n2):
    n1=num(n1)
    n2=num(n2)
    if operator == "-":
        a=n1-n2
        print(a)
    elif operator == "+":
        a=n1+n2
        print(a)
    elif operator == "*":
        a=n1*n2
        print(a)
    elif operator == "/":
        if n2 == 0:
            print("Are you kidding me ? You can not divide by zero")
            n2 = input("Enter the number2: you remember no zero here: ")
            n2 = float(n2)
            a = n1 / n2
            print(a)
        else:
            a=n1/n2
            print(a)
    else:
        print("Please correct the inputed operator")

calculation(oper, num_1, num_2)