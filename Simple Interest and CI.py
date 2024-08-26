def simpleInt(P, R, T):
    simple_interest = (P*R*T) / 100
    print("The Simple Interest is", simple_interest)
def compInt(P, R, T):
    A = P*(1+(R/100))**T
    compound_interest = A-P
    print("The Compund Interest is", compound_interest)

while True:
    print("1.Simple Interest \n2.Compund interest")
    S = int(input("Enter Your Choice of Operation :"))
    P = float(input("Enter Principle :"))
    R = float(input("Enter Rate :"))
    T = float(input("Enter Time :"))

    if S== 1 :
        simpleInt(P,R,T)
    elif S==2:
        compInt(P, R, T)
    else:
        print("Invalid Input")

def sum(a,b):
    return a+b
