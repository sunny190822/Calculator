# I am going to write a basic calculator in pyton that can perfotm addition, subtraction, multiplicaton, division
while True: 
    print ("Welcome to the basic calculator!")
   # a = "addition"
   # b = "subtraction"
    #c = "multiplication"
   # d = "division"
   # e = "average of two numbers"
    print ("What operation would you like to perform? Please choose from the following: addition, subtraction, multiplication, division, average of two numbers")
    operation = input().lower()
    if operation == a:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The result is:", result)
    elif operation == b:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("The result is:", result)
    elif operation == c:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("The result is:", result)
    elif operation == d:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 != 0:
            result = num1 / num2
            print("The result is:", result)
        else:
            print("Error: Division by zero is not allowed.")
    elif operation == e:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = (num1 + num2) / 2
        print("The average is:", result)
    print("Do you want to perform another calculation? (yes/no)")
    answer = input().lower()
    if answer != "yes":
        print("Thank you for using the basic calculator. Goodbye!")
        break