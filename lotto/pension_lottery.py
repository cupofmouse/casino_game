import random

gogo=True
tmp1=0
money=0
attempts=0

def lotto_machine():
    ltt=[]
    for i in range(0,6):
        ltt.append(random.randint(1,9))
    return ltt

def same_num(tmp,ps,jo):
    for i in range(5,-1,-1):
        if ps_lotto[i]==ps[i]:
            tmp+=1
        else:
            break

    global money

    if tmp==6 and jo==ps_jo:
        print(" +"+str(7000000*20*12),"1등 당첨!!")
        money+=(7000000*20*12)
    elif tmp==6 or ps==ps_bn:
        print(" +"+str(1000000*10*12),"2등 당첨!")
        money+=(1000000*10*12)
    elif tmp==5:
        print(" +"+str(1000000),"3등 당첨!")
        money+=1000000
    elif tmp==4:
        print(" +"+str(100000),"4등 당첨!")
        money+=100000
    elif tmp==3:
        print(" +"+str(50000),"5등 당첨!")
        money+=50000
    elif tmp==2:
        print(" +"+str(5000),"6등 당첨!")
        money+=5000
    elif tmp==1:
        print(" +"+str(1000),"7등 당첨!")
        money+=1000
    else:
        print(" 낙첨")


while gogo:
    attempts+=1
    ps_lotto=lotto_machine()
    ps_jo=random.randint(1,5)
    ps_bn=lotto_machine()


    ps_1=lotto_machine()
    jo_1=1
    jo_2=2
    jo_3=3
    jo_4=4
    jo_5=5

    print()
    print(">>당첨 번호<<")
    print(str(ps_jo)+"조",ps_lotto)
    print("))보너스 번호((")
    print("각 조",str(ps_bn))
    print()

    print("*당신의 번호*")
    print(str(jo_1)+"조",str(ps_1))
    print(str(jo_2)+"조",str(ps_1))
    print(str(jo_3)+"조",str(ps_1))
    print(str(jo_4)+"조",str(ps_1))
    print(str(jo_5)+"조",str(ps_1))

    print()

    print("$일치 여부$")
    print()
    same_num(tmp1,ps_1,jo_1)
    same_num(tmp1,ps_1,jo_1)
    same_num(tmp1,ps_1,jo_1)
    same_num(tmp1,ps_1,jo_1)
    same_num(tmp1,ps_1,jo_1)

    print()

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