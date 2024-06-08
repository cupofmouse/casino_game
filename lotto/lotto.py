import random

lotto_number=[]

for i in range(0,6):
    lotto_number.append(random.randint(1,45))

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
elif tmp1==6:
    print(" 1등 당첨!!")
elif tmp1==4:
    print(" 4등 당첨!")
elif tmp1==3:
    print(" 5등 당첨!")
else:
    print(" 낙첨")
    
print()

print("2) ",end="")
for i in range(0,6):
    if ltt_num2[i] in lotto_number:
        print(ltt_num2[i],end=" O ")
    else:
        print(ltt_num2[i],end=" X ")
if tmp2==5:
    print(" 3등 당첨!")
elif tmp2==6:
    print(" 1등 당첨!!")
elif tmp2==4:
    print(" 4등 당첨!")
elif tmp2==3:
    print(" 5등 당첨!")
else:
    print(" 낙첨")

print()

print("3) ",end="")
for i in range(0,6):
    if ltt_num3[i] in lotto_number:
        print(ltt_num3[i],end=" O ")
    else:
        print(ltt_num3[i],end=" X ")
if tmp3==5:
    print(" 3등 당첨!")
elif tmp3==6:
    print(" 1등 당첨!!")
elif tmp3==4:
    print(" 4등 당첨")
elif tmp3==3:
    print(" 5등 당첨")
else:
    print(" 낙첨")

print()

print("4) ",end="")
for i in range(0,6):
    if ltt_num4[i] in lotto_number:
        print(ltt_num4[i],end=" O ")
    else:
        print(ltt_num4[i],end=" X ")
if tmp4==5:
    print(" 3등 당첨!")
elif tmp4==6:
    print(" 1등 당첨!!")
elif tmp4==4:
    print(" 4등 당첨!")
elif tmp4==3:
    print(" 5등 당첨!")
else:
    print(" 낙첨")

print()

print("5) ",end="")
for i in range(0,6):
    if ltt_num5[i] in lotto_number:
        print(ltt_num5[i],end=" O ")
    else:
        print(ltt_num5[i],end=" X ")
if tmp5==5:
    print(" 3등 당첨!")
elif tmp5==6:
    print(" 1등 당첨!!")
elif tmp5==4:
    print(" 4등 당첨!")
elif tmp5==3:
    print(" 5등 당첨!")
else:
    print(" 낙첨")