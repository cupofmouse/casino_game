import random
import copy
from chinchiro_num import *
import string

print("_______________________________")
print("$$$$$$$$               $$$$$$$$")
print("$$$$$$                   $$$$$$")
print("$$$$                       $$$$")
print("$$ 친치로 게임을 시작합니다. $$")
print("oo                           oo")
print("$$$                         $$$")
print()

attempts=0
gogo=1
o_dish=0
o_get=0
e_dish=0
e_get=0
#점수 게임
score_game_num=random.randint(3,10)
score_game=random.sample(range(5,70),score_game_num)
#참가자 인원 수, 판돈 리스트, 돈 리스트, 점수 리스트 초기화
Big_alpha=string.ascii_uppercase
players=[]
for i in range(0,26):
    players.append(Big_alpha[i])
plynum=2
while plynum==2:
    players_num=int(input("당신을 포함해 몇 명의 참가자와 겨루시겠습니까? (2~4명 권장) : "))
    if players_num<2 or players_num>4:
        print("친치로는 보통 2~4명이 플레이하길 권장합니다. 정말로 이 인원대로 진행하시겠습니까?")
        plynum=int(input("1> 계속한다. 2> 인원 수를 조정한다. >> "))
    else:
         plynum=1

players_list=players[:players_num-1]
coma_list=[0]*players_num
money_list=[0]*players_num
score_list=[0]*players_num 

#판돈 리스트
comamch=[]
for i in range(100,30000,500):
    comamch.append(i)

print("당신은",str(players_list)+"와 게임합니다.")
players_list.insert(0,'Y')
input("$")

while gogo:

    if attempts==0:
        #초기 돈 정하기
        moneylist=[]
        for i in range(10000,100000,5000):
            moneylist.append(i)
        money_list[0]=int(input("(10,000~100,000) 당신이 가져온 돈: "))
        for i in range(1,players_num):
            money_list[i]=random.choice(moneylist)
            print(players_list[i]+"가 가져온 돈:",money_list[i])
        org_money=copy.deepcopy(money_list)
        
        input("$")
        print("당신은 Y입니다.")
        print("순서는",str(players_list)+"입니다.")
        print()
    #판돈 정하기
    for i in range(0,players_num):
        coma_list[i]=random.choice(comamch)

    turn=attempts%players_num
    
    #차례가 된 사람이 돈 남아 있을 때
    if money_list[turn]>0:
        input("$")
        print(">>"+players_list[turn]+"의 차례입니다.<<")
        print()
        for i in range(0,players_num):
            if money_list[i]>0:
                if i==turn:
                    coma_list[i]=0
                    continue
                if players_list[i]=='Y':
                    coma_list[i]=int(input("Y가 걸 돈>> "))
                print(players_list[i]+"가 건 돈:",coma_list[i])
                money_list[i]-=coma_list[i]
            else:
                print(players_list[i]+"가 건 돈: 0")
                coma_list[i]=0

        input("$")
        print(players_list[turn],"가 주사위를 굴립니다.")
        dice_list=[]
        for i in range(0,3):
            dice_list.append(random.randint(1,6))
        print(dice_list)
        dice_list.sort()
        input("$")

        if dice_list==pinjoro:
                print("핀조로! 각자 건 말의 5배를 가져가십시오.")
                money_list[turn]+=sum(coma_list)*5
                for i in range(0,players_num):
                    money_list[i]-=coma_list[i]*4
        elif (dice_list==arasi2 or dice_list==arasi3 
              or dice_list==arasi4 or dice_list==arasi5 or dice_list==arasi6): 
                print("아라시! 각자 건 말의 3배를 가져가십시오.")
                money_list[turn]+=sum(coma_list)*3
                for i in range(0,players_num):
                    money_list[i]-=coma_list[i]*2
        elif dice_list==sigoro:
                print("시고로! 각자 건 말의 2배를 가져가십시오.")
                money_list[turn]+=sum(coma_list)*2
                for i in range(0,players_num):
                    money_list[i]-=coma_list[i]
        elif (dice_list==six_eye1 or dice_list==six_eye2 
              or dice_list==six_eye3 or dice_list==six_eye4 or dice_list==six_eye5):
                print("6이 있는 눈있음! 각자 건 말을 가져가십시오.")
                money_list[turn]+=sum(coma_list)
        elif (dice_list==one_eye6 or dice_list==one_eye2 
              or dice_list==one_eye3 or dice_list==one_eye4 or dice_list==one_eye5):
                print("1이 있는 눈있음! 다른 참여자가 건 만큼의 말을 지불하십시오.")
                money_list[turn]-=sum(coma_list)
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]*2
        elif dice_list==hihoomi:
                print("히후미! 다른 참여자가 건 2배 만큼의 말을 지불하십시오.")
                money_list[turn]-=sum(coma_list)*2
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]*3
        elif (dice_list==two_eye1 or  dice_list==two_eye6 
              or dice_list==two_eye3 or dice_list==two_eye4 or dice_list==two_eye5):
                print("2가 있는 눈있음! 2점을 얻습니다.")
                score_list[turn]+=2
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]
        elif (dice_list==three_eye1 or  dice_list==three_eye6 or dice_list==three_eye2 or dice_list==three_eye4 or dice_list==three_eye5):
                print("3이 있는 눈있음! 3점을 얻습니다.")
                score_list[turn]+=3
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]
        elif (dice_list==four_eye1 or  dice_list==four_eye2 or dice_list==four_eye3 or dice_list==four_eye6 or dice_list==four_eye5):
                print("4가 있는 눈있음! 4점을 얻습니다.")
                score_list[turn]+=4
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]
        elif (dice_list==five_eye1 or  dice_list==five_eye2 or dice_list==five_eye3 or dice_list==five_eye4 or dice_list==five_eye6):
                print("5가 있는 눈있음! 5점을 얻습니다.")
                score_list[turn]+=5
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]
        elif dice_list==odd:
            if o_get==0:
                print("홀수눈! 모두 그릇에 말들을 모으십시오.")
                coma_list[turn]=random.choice(comamch)
                money_list[turn]-=coma_list[turn]
                print("룰렛을 돌려",players_list[turn]+"의 말을 정합니다. >>",coma_list[turn])
                o_dish+=sum(coma_list)
                o_get+=1
            elif o_get==1:
                print("홀수눈! 그릇에 담긴 말들을 모두 가져가십시오.")
                money_list[turn]+=o_dish
                for i in range(0,players_num):
                    money_list[i]+=coma_list[i]
                o_dish, o_get=0,0
        elif dice_list==even:
            if e_get==0:
                print("짝수눈! 모두 그릇에 말의 2배를 모으십시오.")
                coma_list[turn]=random.choice(comamch)
                money_list[turn]-=coma_list[turn]*2
                print("룰렛을 돌려",players_list[turn]+"의 말을 정합니다. >>",str(coma_list[turn])+"X2")
                e_dish+=sum(coma_list)*2
                for i in range(0,players_num):
                    money_list[i]-=coma_list[i]
                e_get+=1
            elif e_get==1:
                print("짝수눈! 그릇에 담긴 말들을 모두 가져가십시오.")
                money_list[turn]+=e_dish
                for i in range(0,players_num):
                    money_list[i]-=coma_list[i]
                e_dish, e_get=0,0
        else:
            print("눈없음!")
            for i in range(0,players_num):
                money_list[i]+=coma_list[i]
        print()
        for i in range(0,players_num):
            print(players_list[i]+"의 돈:",money_list[i]    ,"점수:",score_list[i])

        if (dice_list==pinjoro or dice_list==arasi2 or dice_list==arasi3
            or dice_list==arasi4 or dice_list==arasi5 or dice_list==arasi6 or dice_list==sigoro
        or dice_list==six_eye1 or dice_list==six_eye2 or dice_list==six_eye3 or 
        dice_list==six_eye4 or dice_list==six_eye5):
            if players_list[turn]=='Y':
                gogo=int(input(players_list[turn]+"님, 계속하시겠습니까?   1)계속한다 2)그만한다\n >> "))
            else:
                print(players_list[turn]+"님 계속하시겠습니까?   1)계속한다 2)그만한다\n >> ",end="")
                go_go=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
                gogo=random.choice(go_go)
            if gogo==2:
                print(gogo,"\n게임 끝.")
                for i in range(0,players_num):
                    print(players_list[i]+"의 돈:",money_list[i]    ,"딴 돈:",str(money_list[i]-org_money[i]))
                input("$")
                break
            elif gogo==1:
                zero=0
                for i in range(0,players_num):
                     if turn==i:
                          continue
                     elif money_list[i]<=0:
                          zero+=1
                if zero==players_num-1:
                    print(str(gogo),"\n"+players_list[turn]+"가 이겼습니다.")
                    print(players_list[turn]+"의 돈:",money_list[turn]    ,"딴 돈:",money_list[turn]-org_money[turn],)
                    print()
                    print(players_list[0]+"가 딴 돈:",money_list[0]-org_money[0])
                    break
                print(str(gogo),"다음 턴으로 넘어갑니다.")

        else:
            zero=0
            for i in range(0,players_num):
                if turn==i:
                    continue
                elif money_list[i]<=0:
                    zero+=1
            if zero==players_num-1:
                print(str(gogo),"\n"+players_list[turn]+"가 이겼습니다.")
                print(players_list[turn]+"의 돈:",money_list[turn]    ,"딴 돈:",money_list[turn]-org_money[turn],)
                print()
                print(players_list[0]+"가 딴 돈:",money_list[0]-org_money[0])
                break
            print("다음 턴으로 넘어갑니다.")
            input("$")

    if attempts in score_game:
        print()
        print("랜덤 확률로 점수 게임을 시작합니다!")
        print("참가자들중 가장 많은 점수를 가지고 있는 사람에게 나머지가 말을 지불합니다.")
        input("$")
        print()
        print("현재 점수>>\n")
        for i in range(0,players_num):
            print(players_list[i]+":",str(score_list[i])+"점")
        print()
        same=all(x==score_list[0] for x in score_list)
        if same:
            print("모두의 점수가 같으므로 이번 점수 게임은 무승부입니다.")
            input("$")
            print()
            attempts+=1
        else:
            price=[]
            for i in range(0,players_num):
                if money_list[i]>0:
                    price.append(random.randint(0,round(money_list[i]*0.75)))
                else:
                    price.append(0)
            top_score=max(score_list)
            top_num=0

            for i in range(0,players_num):
                if top_score==score_list[i]:
                    print(players_list[i]+"의 점수가 가장 높습니다.")
                    price[i]=0
                    top_num+=1
            print("지불할 상금을 룰렛을 돌려 정합니다. >>",end=" ") 
            for i in range(0,players_num):
                print(players_list[i]+":",str(price[i]),end=" ")
                money_list[i]-=price[i]
            for i in range(0,players_num):    
                if top_score==score_list[i]:
                    money_list[i]+=round(sum(price)/top_num)
                score_list[i]=0
        
            print()
            for i in range(0,players_num):
                print(players_list[i]+"의 돈:",money_list[i]    ,"점수:",score_list[i])
            input("$")

    attempts+=1
    print()
