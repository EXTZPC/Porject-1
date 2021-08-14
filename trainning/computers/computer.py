def S():
    # def S1(a1,n,d):
    #     an=a1+d*(n-1)   
    #     A=n*(a1+an)/2
    #     return A
    def S1(a1,n,d):
        A=n*(a1*2+d*(n-1))/2
        return A
    def S2(a1,n,an):
        d=(an-a1)/(n-1)
        A=n*(a1*2+d*(n-1))/2
        return A
    def S3(n,d,an):
        a1=an-d*(n-1)
        A=n*(a1*2+d*(n-1))/2
        return A
    Q2=input("已知條件:(a1/n/d/an) ")
    if Q2=="a1/n/d":
        print( 
            S1(int(input("輸入首項: ")),
            int(input("輸入項數: ")),
            int(input("輸入公差: ")))
            )
    elif Q2=="a1/n/an":
        print( 
            S2(int(input("輸入首項: ")),
            int(input("輸入項數: ")),
            int(input("輸入末項: ")))
            )
    elif Q2=="n/d/an":
        print( 
            S3(int(input("輸入項數: ")),
            int(input("輸入公差: ")),
            int(input("輸入末項: ")))
            )
    else:
        print("""Input error...請檢察格式
    要照順序輸入""")
