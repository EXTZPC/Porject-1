def M2():
    print("""目錄:
M2-EZ=簡單運算
M2-BMI=BMI
M2-N=n!
----------------""")
    Q2=(input("選擇雲算值:(EZ/BMI/N) "))
    if Q2=="EZ":
        EZ()
    elif Q2=="BMI":
        BMI()
    elif Q2=="N":
        N()
    else:
        print("Input error...")
def EZ():
    Q3=input('選擇運算位數:(2/3): ')
    if Q3=="2":
        n1=int(input("1st number: "))
        n2=int(input("2nd number: "))
        op1=input("運算符號: ")
        if op1=="+":
            print(n1+n2)   
        elif op1=="-":
            print(n1-n2)   
        elif op1=="*":
            print(n1*n2)   
        elif op1=="/":
            print(n1/n2)
        else:
            print("Input error...不支援此運算符號")
    elif Q3=="3":
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
            else:
                print("Input error...不支援此運算符號")
        elif op1=="-":
            if op2=="+":
                print(n1-n2+n3)
            elif op2=="-":
                print(n1-n2-n3)
            elif op2=="*":
                print(n1-n2*n3)
            elif op2=="/":
                print(n1-n2/n3)
            else:
                print("Input error...不支援此運算符號")
        elif op1=="*":
            if op2=="+":
                print(n1*n2+n3)
            elif op2=="-":
                print(n1*n2-n3)
            elif op2=="*":
                print(n1*n2*n3)
            elif op2=="/":
                print(n1*n2/n3)
            else:
                print("Input error...不支援此運算符號")
        elif op1=="/":
            if op2=="+":
                print(n1/n2+n3)
            elif op2=="-":
                print(n1/n2-n3)
            elif op2=="*":
                print(n1/n2*n3)
            elif op2=="/":
                print(n1/n2/n3)
            else:
                print("Input error...不支援此運算符號")
        else:
            print("Input error...不支援此運算符號")
    else:
        print("Input error...不支援此運算位數")
def BMI():
    height=(float(input("輸入身高:(公分) ")))
    weight=(float(input("輸入體重:(公斤) ")))
    n=weight/(height*0.01)**2
    if n<18.5:
        print(n,"(體重過輕)")
    elif 18.5<=n<24:
        print(n,"(體重適中)")
    elif 24<=n<27:
        print(n,"(體重過重)")
    elif n>=27:
        print(n,"(體重超重)")
def N():
    n=int(input("請輸入n: "))
    M=1
    N=1
    for x in range(n):
        N*=M
        M+=1
    else:
        print(N)