def N7():
    Q2=input("輸入題號: ")
    if Q2=="1":
        N7_1()
    elif Q2=="2":
      N7_2()
    elif Q2=="3":
        N7_3()
    elif Q2=="4":
        N7_4()
    elif Q2=="5":
        N7_5()
    elif Q2=="6":
        N7_6()
    elif Q2=="7":
        N7_7()
    elif Q2=="8":
        N7_8()
    elif Q2=="9":
        N7_9()
    else:
        print("Input error...")
def N7_1():
    print("""溫度轉換器
----------------""")
    Q3=input("F-C/C-F ")
    if Q3=="C-F":
        C=int(input("請輸入攝氏溫度: "))
        print(
            9/5*C+32
        )
    elif Q3=="F-C":
        F=int(input("請輸入華氏溫度: "))
        print(
            5/9*(F-32)
        )
    else:
        print("Input error...")
def N7_2():
    print("""等第轉換器
----------------""")
    N=int(input("輸入分數: "))
    if 90<=N<=100:
        print("A")
    elif 80<=N<90:
        print("B")
    elif 70<=N<80:
        print("C")
    elif 60<=N<70:
        print("D")
    elif 0<=N<60:
        print("E")
    else:
        print("Input error...")
def N7_3():
    print("""長度單位轉換器(呎/公分)
----------------""")
    Q3=input("inch-centimeter/centimeter-inch ")
    if Q3=="inch-centimeter":
        inchx12=int(input("請輸入 呎: "))
        inch=int(input("請輸入 吋: "))
        print(
            (inch+inchx12*12)*2.54,"公分"
        )
    elif Q3=="centimeter-inch":
        centimeter=int(input("請輸入 公分: "))
        inch=centimeter/2.54
        print(
            inch//12,"呎",inch%12,"吋"
        )
    else:
        print("Input error...")
def N7_4():
    print("""匯率兌換器(台-日) 
手續費=5%
----------------""")
    money=int(input("輸入 元: "))
    Q3=input("選擇幣值:(台/日) ")
    if Q3=="台":
        print(
            (money*3.5)*0.95,"JPY"
        )
    elif Q3=="日":
        print(
            (money/3.5)*0.95,"NTD"
        )
    else:
        print("Input error...")
def N7_5():
    print("""判斷式
----------------""")
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
def N7_6():
    n=int(input("請輸入n: "))
    M=1
    A=1
    for x in range(n):
        A*=M
        M+=1
    else:
        print(A)
def N7_7():
    print("""無意義的題目
----------------""")
    for x in range(1001):
        if x%3!=2:
            continue
        elif x%7!=2:
            continue
        elif x%11!=2:
            continue
        print(x)
def N7_8():
    import random as R
    print("""猜識字機(1~100)
----------------""")
    x=int(R.choice(range(1,101)))
    A=int(input("請猜數字: "))
    n=1
    while A!=x:
        if A>x:
            print("Wrong! 你猜",n,"次囉! 再小一點!")
        elif A<x:
            print("Wrong! 你猜",n,"次囉! 再大一點!")
        n+=1
        A=int(input("猜猜數字: "))
    else:
        print("Bingo! 你共猜了",n,"次!")
def N7_9():
    print("""計程車收費跳表
----------------""")
    x=int(input("輸入里程數(公尺): "))
    if x>1500:
        if x/250==x//250:
            print(
                75+5*((x-1500)//250),"元"
            )
        elif x/250!=x//250:
            print(
                75+5*((x-1500)//250+1),"元"
            )
    elif x<=1500:
        print("75 元")