import subprocess

num=1
while num:
    print()
    print("*$>로또 상점에 어서오세요<$*")
    print()
    num=int(input("1) 6/45 복권 사기\n2) 연금 복권 사기\n3)나가기\n>>"))

    file_adv_lotto_mch_path="adv_lotto_mch.py"
    file_pension_lottery_path="pension_lottery.py"

    if num==1:
        subprocess.run(["python",file_adv_lotto_mch_path])
    elif num==2:
        subprocess.run(["python",file_pension_lottery_path])
    elif num==3:
        print("안녕히가세요!")
        num=0
    else:
        print("그런 복권 없습니다.")
        
