import random as rd

def Valorant_R():
    Valorant=(
        "Jett","Raze","Sova",
        "Reyna","Phoenix","Viper",
        "Cypher","Brimstone","Omen",
        "Breach","Astra","Yoru",
        "Killjoy","Sage","Kay-o"
    )
    L3="A","B","C","D","E",
    Q=int(input("雖機選取(1/2~5)個角色:"))
    if Q==1:
        print(
            rd.choice(Valorant)
        )
    elif 2<=Q<=5:
        print(
            rd.sample(Valorant,Q)
        )
    else:
        print("Inpu error...")

def Ans_R():
    R1=[]
    Anss="A","B","C","D","E",
    for n in range(int(input("random times: "))):
        m=[rd.choice(Anss)]
        R1.extend(m)
    else:
        print(R1)

def If_R():
    print(rd.choice(["Y","N"]))

print(
    """~。~目錄~。~
    隨機選取角色：
    瓦羅蘭=Valorant
    
    隨機選取答案：
    選擇題=Ans
    是非題=If"""
)
User_Q=input("randompick for...")
if User_Q=="Valorant" or User_Q=="V":
    Valorant_R()
elif User_Q=="Ans" or User_Q=="A":
    Ans_R()
elif User_Q=="If" or User_Q=="I":
    If_R()
else:
    print("Inpu error...")