import random
word = []

print("How long should the password be? (enter a number)")
n = int(input())

def bu(num):
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        word.append(sp)


while True:
    bu(n)
    print("".join(word))
    word = []
    print("Another password? Enter the length to continue or leave with NO")
    k = str(input())
    try:
        n = int(k)
    except:
        print("Goodbye! Do you want to know how save your new password is?")
        print('Go to the repository "medium-sized-projects" and find the answer with the')
        print("passwordStrength_demo")
        break
    
 