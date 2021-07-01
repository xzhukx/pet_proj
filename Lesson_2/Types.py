num_1 = input("Enter the number1: ")
operator = input("Enter the operator: ")
num_2 = input("Enter the number2: ")

try:
    num_1 = float(num_1)
except Exception as e:
    print(e)
    exit()

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operator == "-":
        a=num_1-num_2
        print(a)
    elif operator == "+":
        a=num_1+num_2
        print(a)
    elif operator == "*":
        a=num_1*num_2
        print(a)
    elif operator == "/":
        a=num_1/num_2
        print(a)
    else:
        print("Incorrect operator")
else:
    print("Please print integer")
