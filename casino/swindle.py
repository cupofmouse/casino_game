import random

print("   *****  ")
print("  ******* ")
print(" **야바위**")
print("************")
print()
attempts=0
gogo=1
money=[]
tmp=[]

while gogo:
    num=int(input("개수: "))+1
    money.append(int(input("얼마를 거시겠습니까? > ")))
    tmp.append(money[attempts])

    for i in range(1,num):
        print(str(i)+")")
        for x in range(1,4):
            for y in range(1,4,x):
                print(" ",end="")
            for z in range(1,2*x+1):
                print("@",end="")
            print()
        print()

    ans=random.randint(1,num-1)
    ply=int(input("어디에 있을까? > "))

    if ans==ply:
        print("정답!")
        money[attempts]*=(num-1)
    else:
        print("오답!")
        money[attempts]=0
    attempts+=1
    print()
    gogo=int(input("계속 하시겠습니까?\n 1)계속한다  0)그만한다 > "))
    print()

ttotal=sum(tmp)
total=sum(money)
print("각 회차 건 돈:",tmp)
print("총:",ttotal)
print("각 회차 얻은 돈:", money)
print("얻은 금액:",total)
print("총 이익:",total-ttotal)