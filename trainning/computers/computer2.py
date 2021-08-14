def C2():
    print("""目錄:
C2-D=開根號
C2-XY=二元一次方程式
----------------""")
    Q2=input("選擇運算值:(D/XY) ")
    if Q2=="D":
        X=(int(input("1st number: ")))
        print(X**0.5) 
    elif Q2=="XY":
        print("""目錄:
C2-Dis=點距
C2-^2=圖形面積
C2-DXY=求直線方程式
----------------""")
        Q3=input("選擇運算值:(Dis/^2/DXY) ")
        if Q3=="Dis":
            x1=int(input("(分別輸入 x1 y1 x2 y2)x1= "))
            y1=int(input("y1="))
            x2=int(input("x2="))
            y2=int(input("y2="))
            print(((x1-x2)**2+(y1-y2)**2)**0.5)
        elif Q3=="^2":
            Q4=input("幾邊形的面積:(3/4/5/6) ")
            if Q4=="3":
                x1=int(input("(分別輸入 x1 y1 x2 y2 x3 y3)x1= "))
                y1=int(input("y1="))
                x2=int(input("x2="))
                y2=int(input("y2="))
                x3=int(input("x3="))
                y3=int(input("y3="))
                print(
                    ((((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))**2)**0.5)/2
                )
            elif Q4=="4":
                x1=int(input("(分別輸入 x1 y1 x2 y2 x3 y3 x4 y4)x1= "))
                y1=int(input("y1="))
                x2=int(input("x2="))
                y2=int(input("y2="))
                x3=int(input("x3="))
                y3=int(input("y3="))
                x4=int(input("x4="))
                y4=int(input("y4="))
                print(
                    ((((x1*y2+x2*y3+x3*y4+x4*y1)-(x2*y1+x3*y2+x4*y3+x1*y4))**2)**0.5)/2
                )
            elif Q4=="5":
                x1=int(input("(分別輸入 x1 y1 x2 y2 x3 y3 x4 y4 x5 y5)x1= "))
                y1=int(input("y1="))
                x2=int(input("x2="))
                y2=int(input("y2="))
                x3=int(input("x3="))
                y3=int(input("y3="))
                x4=int(input("x4="))
                y4=int(input("y4="))
                x5=int(input("x5="))
                y5=int(input("y5="))
                print(
                    ((((x1*y2+x2*y3+x3*y4+x4*y5+x5*y1)-(x2*y1+x3*y2+x4*y3+x5*y4+x1*y5))**2)**0.5)/2
                )
            elif Q4=="6":
                x1=int(input("(分別輸入 x1 y1 x2 y2 x3 y3 x4 y4 x5 y5 x6 y6)x1= "))
                y1=int(input("y1="))
                x2=int(input("x2="))
                y2=int(input("y2="))
                x3=int(input("x3="))
                y3=int(input("y3="))
                x4=int(input("x4="))
                y4=int(input("y4="))
                x5=int(input("x5="))
                y5=int(input("y5="))
                x6=int(input("x6="))
                y6=int(input("y6="))
                print(
                    ((((x1*y2+x2*y3+x3*y4+x4*y5+x5*y6+x6*y1)-(x2*y1+x3*y2+x4*y3+x5*y4+x6*y5+x1*y6))**2)**0.5)/2
                )
            else:
                print("Input error...")
        elif Q3=="DXY":
            x1=int(input("(分別輸入 x1 y1 x2 y2)x1= "))
            y1=int(input("y1="))
            x2=int(input("x2="))
            y2=int(input("y2="))
            n=x1-x2
            m=y1-y2
            k=x1*y2-x2*y1
            print(n,"y=",m,"x-",k)
        else:
            print("Input error...")
    else:
        print("Input error...")