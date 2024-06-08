visit=1

print()
print("*$>카지노에 어서오세요<$*")
print()

sw_total, sw_ttotal, oo_total, oo_ttotal=0,0,0,0
pay_total, get_total=0,0
money_list=[0]
org_money=[0]
players_list=[0]
bet_list=[0]

while visit:
    print()
    num=int(input("1) 야바위\n2) 홀짝 게임\n3) 친치로\n4) 슬롯 머신\n5) 러시안 룰렛\n6) 나가기\n>>"))

    if num==1:
        print()
        from swindle import total as sw_total, ttotal as sw_ttotal
    elif num==2:
        print()
        from oddoreven import total as oo_total, ttotal as oo_ttotal
    elif num==3:
        print()
        from chinchiro import money_list, org_money
    elif num==4:
        print()
        from slot_mch import pay_total, get_total
    elif num==5:
        print()
        from russian_roulette import players_list, org_players_list, org_bet_list, bet_list, goodbye
        if goodbye==1:
            break
    elif num==6:
        print()
        print("안녕히가세요!")
        visit=0
    else:
        print("그런 게임 없습니다.")

my_bet=bet_list[players_list.index('Y')]
org_bet=org_bet_list[org_players_list.index('Y')]

sum1=sw_total+oo_total+org_money[0]+org_bet+pay_total
sum2=sw_ttotal+oo_ttotal+money_list[0]+my_bet+get_total
print("당신이 들고간 돈:",sum1)
print("카지노에서 들고 나온 돈:",sum2)
if goodbye==1:
    print("최종 이익: 0")
else:
    print("최종 이익:",str(sum2-sum1))