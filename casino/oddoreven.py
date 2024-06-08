import random

print(" oO         OoO")
print("oo            Oo")
print("  ^^홀짝 게임^^")
print(" oO           O")
gogo=1
money=[]
attempts=0
tmp=[]

while gogo:
    print()
    money.append(int(input("얼마를 거시겠습니까? >> ")))
    tmp.append(money[attempts])
    print()
    ply=int(input("1.홀? 0.짝? >> "))
    marble=random.randint(1,10)
    ood=marble%2

    if ood==1 and ood==ply:
        print("구슬의 개수:",str(marble))
        print("홀, 정답!")
        money[attempts]*=2
    elif ood==0 and ood==ply:
        print("구슬의 개수:",str(marble))
        print("짝, 정답!")
        money[attempts]*=2
    elif ood==1:
        print("구슬의 개수:",str(marble))
        print("홀, 오답!")
        money[attempts]*=-1
    elif ood==0:
        print("구슬의 개수:",str(marble))
        print("짝, 오답!")
        money[attempts]*=-1
    attempts+=1
    print()
    gogo=int(input("계속 하시겠습니까?\n  1)계속한다 0)그만한다 >> "))

ttotal=sum(tmp)
total=sum(money)
print()
print("각 회차 당신이 건 돈:",tmp)
print("총 건 돈:",ttotal)
print("각 회차 결과:",money)
print("당신이 얻은 돈:",total)
print("총 이익:",total-ttotal)

