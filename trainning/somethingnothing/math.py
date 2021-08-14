n1=int(input("1st number: "))
n2=int(input("2nd number: "))
n3=int(input("3rd number: "))
op1=input("運算符號1: ")
op2=input("運算符號2: ")
if op1=="+":
    if op2=="+":
        print(n1+n2+n3)
    elif op2=="-":
        print(n1+n2-n3)
    elif op2=="*":
        print(n1+n2*n3)
    elif op2=="/":
        print(n1+n2/n3)
elif op1=="-":
    if op2=="+":
        print(n1-n2+n3)
    elif op2=="-":
        print(n1-n2-n3)
    elif op2=="*":
        print(n1-n2*n3)
    elif op2=="/":
        print(n1-n2/n3)
elif op1=="*":
    if op2=="+":
        print(n1*n2+n3)
    elif op2=="-":
        print(n1*n2-n3)
    elif op2=="*":
        print(n1*n2*n3)
    elif op2=="/":
        print(n1*n2/n3)
elif op1=="/":
    if op2=="+":
        print(n1/n2+n3)
    elif op2=="-":
        print(n1/n2-n3)
    elif op2=="*":
        print(n1/n2*n3)
    elif op2=="/":
        print(n1/n2/n3)
