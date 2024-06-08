import random
import copy

gogo=True
money=0
attempts=0
tmp1=0
tmp2=0
tmp3=0
tmp4=0
tmp5=0

def ltt_machine():
    a=[]
    for i in range(0,6):
        a.append(random.randint(1,45))
    return a      

def bonus_ltt():
    b=random.randint(1,45)
    return b

def same_num(tmp,ltt_NUM):
    lttn=copy.deepcopy(lotto_number)

    for i in range(0,6):
        if ltt_NUM[i] in lttn:
            print("("+str(ltt_NUM[i]), end=") ")
            tmp+=1
            for x in range(0,6):
                if ltt_NUM[i]==lttn[x]:
                    lttn[x]=0
                    break
        else:
            print("X",end=" ")

    global money

    if tmp==6:
        print(" 1등 당첨!")
        money+=1200000000
    elif tmp==5 and bonus_number in lttn:
        print(" 2등 당첨!")
        money+=79000000
    elif tmp==5:
        print(" 3등 당첨!")
        money+=1400000
    elif tmp==4:
        print(" 4등 당첨!")
        money+=50000
    elif tmp==3:
        print(" 5등 당첨!")
        money+=5000
    else:
        print(" 낙첨")

    
    print()


while gogo:
    attempts+=1
    lotto_number=ltt_machine()
    bonus_number=bonus_ltt()

    print()
    print(">>당첨 번호<<")
    print(lotto_number,"+",bonus_number)
    print()

    ltt_num1=ltt_machine()
    ltt_num2=ltt_machine()
    ltt_num3=ltt_machine()
    ltt_num4=ltt_machine()
    ltt_num5=ltt_machine()
    
    print("*당신의 번호*")
    print(ltt_num1)
    print(ltt_num2)
    print(ltt_num3)
    print(ltt_num4)
    print(ltt_num5)
    print()
    

    print("$일치 여부$")
    print()
    same_num(tmp1,ltt_num1)

    same_num(tmp2,ltt_num2)

    same_num(tmp3,ltt_num3)

    same_num(tmp4,ltt_num4)

    same_num(tmp5,ltt_num5)


    print(str(attempts)+"번째 시도 중")
    print("얻은 금액:",money)
    print("계속 할까요?")
    print("계속 한다> 1     그만한다> 0")
    gogo=int(input(">>> "))

consumption=attempts*5000
print("당첨금:",money)
print("소비한 금액:",consumption)
print("순이익: ",money-consumption)
print("다음에 또 오세요! : )")