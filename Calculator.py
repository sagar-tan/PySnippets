print ("This is our First Class")


def add(a, b):
    return a+b #1
def Subtract(a, b):
    return a-b #1
def multiply(a, b):
    return a*b #1
def divide(a, b):
    return a/b
while True:
    a = int(input("Enter First no : ")) #1
    operator = input("Enter a Operator :")
    b = int(input("Enter Second no : "))

    if operator == "+" or "plus":
            print(add(a,b))
    elif operator == "-":
            print(Subtract(a, b))
    elif operator == "*":
            print(multiply(a, b))
    elif operator == "/":
            if(b!=0):
                print(divide(a, b))
            else:
                print("Invalid Input")
    else :
         print("invalid input")
    
        
