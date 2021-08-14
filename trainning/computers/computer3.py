def C3():
    print("""目錄:
C3-1=一元二次方程式
C3-2=二元二次方程式(二次函數)
----------------""")
    Q2=input("選擇運算值:(1/2) ")
    if Q2=="1":
        C3_1()
    elif Q2=="2":
        C3_2()
    else:
        print("Input error...")
def C3_1():
    print("""目錄:
P=判斷式+解
----------------""")
    Q3=input("選擇運算值:(P/) ")
    if Q3=="P":
        a=int(input("請輸入X**2係數: "))
        b=int(input("請輸入X係數: "))
        c=int(input("請輸入常數: "))
        P=b**2-4*a*c
        if P>0:
            print("相異實根",
                (-b+P**0.5)/(2*a),(-b-P**0.5)/(2*a)
            )
        elif P==0:
            print("重根",
                (-b+P**0.5)/(2*a)
            )
        elif P<0:
            print("虛根")
        else:
            print("Input error...")
    else:
        print("Inpu error...")
def C3_2():
    print("""目錄:
O=求頂點
----------------""")
    Q3=input("選擇運算值:(O/) ")
    if Q3=="O":
        Q4=input("輸入")
        None
