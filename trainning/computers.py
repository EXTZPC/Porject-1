import sys as s
s.path.append("computers")
import computer as S
import math2_0 as M2
import computer2 as C2
import computer3 as C3
import N7_answer as N7

print("""目錄:
C-S=等差級數
C-M2=簡單運算、BMI值...
C-C2=根號、二元一次方程式
C-C3=一元二次、二元二次方程式
C-N7=N7解答區
----------------""")
Q1=input("選擇運算值:(S/M2/C2/C3/N7) ")
if Q1=="S":
    S.S()
elif Q1=="M2":
    M2.M2()
elif Q1=="C2":
    C2.C2()
elif Q1=="C3":
    C3.C3()
elif Q1=="N7":
    N7.N7()
else:
    print("Input error...")
