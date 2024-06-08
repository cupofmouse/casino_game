import random
import time as t

print("       O      ")
print("  @         O ")
print("  러시안 룰렛  ")
print("  O         O ")
print("       O      ")
goodbye=0
playerslist=['A','B','C','D','E','F']
bullet=random.randint(0,5)
plynum=1
while plynum:
    players_num=int(input("당신을 포함해 몇 명과 플레이하시겠습니까? (2,3,6명 제한) >> "))
    if players_num==2 or players_num==3 or players_num==6:
        plynum=0
    else:
        print("이 게임은 2,3,6명이서 해야합니다.")
        input("$")
        print()
players_list=playerslist[:players_num-1]
print("\n당신은",str(players_list)+"와 게임을 합니다.")
players_list.insert(0,'Y')
print("당신은 Y 입니다.")
input("$")

print("각자 가져온 돈의 전액을 겁니다.")
bet_list=[]
for i in range(0,players_num):
    bet_list.append(0)
bet_list[0]=int(input("당신이 걸 돈: "))
for i in range(1,players_num):
    bet_list[i]=random.randint(100000,1000000)
    print(players_list[i]+"가 건 돈:",bet_list[i])
input("$")

print("랜덤으로 순서를 정합니다.")
input("$")
import copy
org_players_list=copy.deepcopy(players_list)
org_bet_list=copy.deepcopy(bet_list)
random.shuffle(players_list)
for i in range(0,players_num):
    where=players_list.index(org_players_list[i])
    tmp=org_bet_list[i]
    bet_list[where]=tmp


print("순서->")
for i in range(0,players_num):
    print(str(i+1)+")",players_list[i])
    t.sleep(1)
print()
print("탄창을 돌립니다.")
input("$")
for i in range(0,3):
    print("철컥")
    t.sleep(1)

print("러시안 룰렛을 시작합니다.")
input("$")
print()

for i in range(0,6):
    print(players_list[i%players_num]+"가 방아쇠를 당깁니다.")
    t.sleep(3)
    if i==bullet:
        print("탕!!!!!!!")
        print("     *  *       ** *  *   *  **")
        print("     *  ** *  ****** *** ** * * *")
        print("    ** **** ********* * * **** *")
        print("   **** ***  **** ***   ***")
        print("     ***** ** **  *** *")
        print("   *********")
        print("  ***         *       ")
        input("$")
        print(players_list[i%players_num]+"는 죽었습니다.")
        print(players_list[i%players_num]+"의 판돈을",str(players_num-1)+"명이서 나눠갖습니다.")
        dead_bet=round(bet_list[i%players_num]/players_num-1)
        for x in range(0,players_num):
            bet_list[x]+=dead_bet
            if x==i%players_num:
                bet_list[i%players_num]=0
            print(players_list[x]+"의 돈:",bet_list[x])
        if players_list[i%players_num]=='Y':
            goodbye=1
        break
    else:
        print("철컥")
        input("$")
        print("빈 탄창이었습니다.")
        print("다음 순서로 넘어갑니다.")
        input("$")