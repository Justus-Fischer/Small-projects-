import random
word = []


def bu(num):
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        word.append(sp)
       
bu(15)
print("".join(word))