num_1 = input("Enter the number1: ")
operator = input("Enter the operator: ")
num_2 = input("Enter the number2: ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
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
        print("Please correct the inputed operator")
except Exception as e:
    print("Please correct the inputed numbers")
    exit()