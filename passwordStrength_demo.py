import random
import time
word = []

print("Type in a password to be tested")
print("(start with short passwords (2-4 characters long))")

pas = str(input())
boost = False
trys = 0
def bu(num):
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        word.append(sp)
 
fi = False
st = time.time()
while fi == False:
    bu(len(pas))
    if "".join(word) == pas:
        break
    else:
        trys = trys + 1
        if trys < 500:
            print("".join(word))
        else:
            if boost == False:
                print("Deactivate output to work faster")
                boost = True
        word = []
        
print("Password cracked after "+ str(trys) +" trys and " + str(time.time() - st) + " seconds or "+ str((time.time()-st)//60) + " minutes.")

    
