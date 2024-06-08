import random  

consume=0
attempts=0
test=True
first=2800000000
second=79000000
third=1500000
fourth=50000
fifth=5000

while test:
    correct=0
    lotto_number=[]
    attempts+=1
    consume+=5000


    for i in range(0,6):
        lotto_number.append(random.randint(1,45))

    print()
    print(">>당첨번호<<")
    print(lotto_number)
    print()

    print("*당신의 번호*")
    ltt_num=[]

    for i in range(0,6):
        ltt_num.append(random.randint(1,45))

    print(ltt_num)

    same_num=6

    for i in range(0,6):
        if ltt_num[i] in lotto_number:
            correct+=1

    if correct==same_num:
        test=False
    
    attempts+=1
    print()
    print("------------------------")

print(str(attempts)+"번째 시도만에 1등")
print("확률: ",str(100/attempts)+"%")
print("순이익: "+str(first-consume))