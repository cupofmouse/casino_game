import random

gogo=True
money=0
attempts=0

while gogo:
    lotto_number=[]
    attempts+=1

    for i in range(0,6):
        lotto_number.append(random.randint(1,45))

    print()
    print(">>당첨번호<<")
    print(lotto_number)
    print()

    ltt_num1=[]
    ltt_num2=[]
    ltt_num3=[]
    ltt_num4=[]
    ltt_num5=[]

    for i in range(0,6):
        ltt_num1.append(random.randint(1,45))
        ltt_num2.append(random.randint(1,45))
        ltt_num3.append(random.randint(1,45))
        ltt_num4.append(random.randint(1,45))
        ltt_num5.append(random.randint(1,45))

    print("*당신의 번호*")
    print(ltt_num1)
    print(ltt_num2)
    print(ltt_num3)
    print(ltt_num4)
    print(ltt_num5)

    print("$일치 여부$")

    tmp1=0
    tmp2=0
    tmp3=0
    tmp4=0
    tmp5=0

    print("1) ",end="")
    for i in range(0,6):
        if ltt_num1[i] in lotto_number:
            print(ltt_num1[i],end=" O ")
            tmp1+=1
        else:
            print(ltt_num1[i],end=" X ")
    if tmp1==5:
        print(" 3등 당첨!")
        money+=1400000
    elif tmp1==6:
        print(" 1등 당첨!!")
        money+=1200000000
    elif tmp1==4:
        print(" 4등 당첨!")
        money+=50000
    elif tmp1==3:
        print(" 5등 당첨!")
        money+=5000
    else:
        print(" 낙첨")
        
    print()

    print("2) ",end="")
    for i in range(0,6):
        if ltt_num2[i] in lotto_number:
            print(ltt_num2[i],end=" O ")
            tmp2+=1
        else:
            print(ltt_num2[i],end=" X ")
    if tmp2==5:
        print(" 3등 당첨!")
        money+=1400000
    elif tmp2==6:
        print(" 1등 당첨!!")
        money+=1200000000
    elif tmp2==4:
        print(" 4등 당첨!")
        money+=50000
    elif tmp2==3:
        print(" 5등 당첨!")
        money+=5000
    else:
        print(" 낙첨")

    print()

    print("3) ",end="")
    for i in range(0,6):
        if ltt_num3[i] in lotto_number:
            print(ltt_num3[i],end=" O ")
            tmp3+=1
        else:
            print(ltt_num3[i],end=" X ")
    if tmp3==5:
        print(" 3등 당첨!")
        money+=1400000
    elif tmp3==6:
        print(" 1등 당첨!!")
        money+=1200000000
    elif tmp3==4:
        print(" 4등 당첨")
        money+=50000
    elif tmp3==3:
        print(" 5등 당첨")
        money+=5000
    else:
        print(" 낙첨")

    print()

    print("4) ",end="")
    for i in range(0,6):
        if ltt_num4[i] in lotto_number:
            print(ltt_num4[i],end=" O ")
            tmp4+=1
        else:
            print(ltt_num4[i],end=" X ")
    if tmp4==5:
        print(" 3등 당첨!")
        money+=1400000
    elif tmp4==6:
        print(" 1등 당첨!!")
        money+=1200000000
    elif tmp4==4:
        print(" 4등 당첨!")
        money+=50000
    elif tmp4==3:
        print(" 5등 당첨!")
        money+=5000
    else:
        print(" 낙첨")

    print()

    print("5) ",end="")
    for i in range(0,6):
        if ltt_num5[i] in lotto_number:
            print(ltt_num5[i],end=" O ")
            tmp5+=1
        else:
            print(ltt_num5[i],end=" X ")
    if tmp5==5:
        print(" 3등 당첨!")
        money+=1400000
    elif tmp5==6:
        print(" 1등 당첨!!")
        money+=1200000000
    elif tmp5==4:
        print(" 4등 당첨!")
        money+=50000
    elif tmp5==3:
        print(" 5등 당첨!")
        money+=5000
    else:
        print(" 낙첨")

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