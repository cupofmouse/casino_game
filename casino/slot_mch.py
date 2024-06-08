import random
import copy

pic_3=['&','$','@']
pic_4=['&','$','@','#']
pic_5=['&','$','@','#','7']
in_slot_machine_room=1
pay_3, pay_4, pay_5=0, 0, 0
get_3, get_4, get_5=0, 0, 0
print()
print("----------------------------------")
print("----------------------------------")
print("||  @   #   $   &   %   *   ^   || ㅇ")
print("||------------------------------|| ㅒ")
print("||  슬롯 머신 룸에 입장합니다.  || ㅒ")
print("||------------------------------|| ㅒ")
print("||  %   *   @   $   #   @   &   ||==")
print("----------------------------------")
print("----------------------------------")
print("세 개의 슬롯 머신이 보인다.")
while in_slot_machine_room:
    print()
    slot=int(input("어떤 머신을 선택할까?\n1) 333 슬롯 2) 444 슬롯 3) 555 슬롯 4)나가기: "))
    if slot==4:
        break

    if slot==1:
        gogo_3=1
        attempts_3=0
        jackpot_3=2500
        get_3=0
        while gogo_3:
            attempts_3+=1
            print("ㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅ")
            print("500원을 넣었습니다.")
            i=random.randint(0,100)
            a=random.randint(0,100)
            b=random.randint(0,100)
            print("---------")
            print("||"+pic_3[i%3], pic_3[a%3], pic_3[b%3]+"|| ㅇ")
            print("||-----|| ㅒ")
            print("||"+pic_3[(i+1)%3], pic_3[(a+1)%3], pic_3[(b+1)%3]+"|| ㅒ")
            print("||-----|| ㅒ")
            print("||"+pic_3[(i+2)%3], pic_3[(a+2)%3], pic_3[(b+2)%3]+"||==")
            print("---------")
            print()
            if (pic_3[(i+1)%3]==pic_3[(a+1)%3] 
                and pic_3[(b+1)%3]==pic_3[(i+1)%3]):
                print("잭팟! 2,500원를 얻습니다.")
                get_3+=jackpot_3
            gogo_3=int(input("레버를 당길까? 1)당긴다 0)당기지 않는다 >> "))
            print()
        pay_3=attempts_3*500
        print("쓴 돈:",pay_3)
        print("얻은 돈:",get_3)
        print("순 이익:",get_3-pay_3)

    if slot==2:
        gogo_4=1
        attempts_4=0
        jackpot_4=50000
        get_4=0
        while gogo_4:
            attempts_4+=1
            print("ㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅ")
            print("500원을 넣었습니다.")
            i=random.randint(0,100)
            a=random.randint(0,100)
            b=random.randint(0,100)
            c=random.randint(0,100)
            print("-----------")
            print("||"+pic_4[i%4], pic_4[a%4], pic_4[b%4], pic_4[c%4]+"|| ㅇ")
            print("||-------|| ㅒ")
            print("||"+pic_4[(i+1)%4], pic_4[(a+1)%4], pic_4[(b+1)%4], pic_4[(c+1)%4]+"|| ㅒ")
            print("||-------|| ㅒ")
            print("||"+pic_4[(i+2)%4], pic_4[(a+2)%4], pic_4[(b+2)%4], pic_4[(c+2)%4]+"||==")
            print("-----------")
            print()
            if (pic_4[(i+1)%4]==pic_4[(a+1)%4]
                and pic_4[(a+1)%4]==pic_4[(b+1)%4]
                and pic_4[(b+1)%4]==pic_4[(c+1)%4]):
                print("잭팟! 50,000원를 얻습니다.")
                get_4+=jackpot_4
            gogo_4=int(input("레버를 당길까? 1)당긴다 0)당기지 않는다 >> "))
            print()
        pay_4=attempts_4*500
        print("쓴 돈:",pay_4)
        print("얻은 돈:",get_4)
        print("순 이익:",get_4-pay_4)

    if slot==3:
        gogo_5=1
        attempts_5=0
        jackpot_5=1000000
        get_5=0
        while gogo_5:
            attempts_5+=1
            print("ㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅ")
            print("500원을 넣었습니다.")
            i=random.randint(0,100)
            a=random.randint(0,100)
            b=random.randint(0,100)
            c=random.randint(0,100)
            d=random.randint(0,100)
            print("-------------")
            print("||"+pic_5[i%5], pic_5[a%5], pic_5[b%5], pic_5[c%5], pic_5[d%5]+"|| ㅇ")
            print("||---------|| ㅒ")
            print("||"+pic_5[(i+1)%5], pic_5[(a+1)%5], pic_5[(b+1)%5], pic_5[(c+1)%5], pic_5[(d+1)%5]+"|| ㅒ")
            print("||---------|| ㅒ")
            print("||"+pic_5[(i+2)%5], pic_5[(a+2)%5], pic_5[(b+2)%5], pic_5[(c+2)%5], pic_5[(d+2)%5]+"||==")
            print("-------------")
            print()
            if (pic_5[(i+1)%5]==pic_5[(a+1)%5]
                and pic_5[(a+1)%5]==pic_5[(b+1)%5]
                and pic_5[(b+1)%5]==pic_5[(c+1)%5]
                and pic_5[(c+1)%5]==pic_5[(d+1)%5]):
                print("잭팟! 1,000,000원를 얻습니다.")
                get_5+=jackpot_5
            gogo_5=int(input("레버를 당길까? 1)당긴다 0)당기지 않는다 >> "))
            print()
        pay_5=attempts_5*500
        print("쓴 돈:",pay_5)
        print("얻은 돈:",get_5)
        print("순 이익:",get_5-pay_5)

pay_total=pay_3+pay_4+pay_5
get_total=get_3+get_4+get_5
print("쓴 돈:",pay_total)
print("얻은 돈:",get_total)
print("순 이익:",get_total-pay_total)