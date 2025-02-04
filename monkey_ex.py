import random
import string
from colorama import init, Fore, Back, Style

init()


alphabet=list(string.ascii_lowercase)
lst=[]
love=['l','o','v','e']

while True:
    x=random.choice(alphabet)
    print(Fore.GREEN+x,end=" ")
    lst.append(x)

    if len(lst)>4:
        if lst[-4:]==love:
            break

print("\nLove found in",str(len(lst)-2))
input()