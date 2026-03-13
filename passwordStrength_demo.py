import random
import time
word = []

def gettime(tr):
    tims = (95**len(pas)) / tr
    if tims > 60:
        tims = tims / 60
        if tims > 60:
            tims = tims / 60
            if tims > 24:
                tims = tims / 24
                if tims > 365:
                    tims = tims / 365
                    if tims > 1000:
                        tims = tims / 1000
                        return str(str(tims) + " milenials")
                    else:
                        return str(str(tims) + " years")
                else:
                    return str(str(tims) + " days")
            else:
                return str(str(tims) + " hours")
        else:
            return str(str(tims) + " minutes")
    else:
        return str(str(tims) + " seconds")
    
    
def bu(num):
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))
    
        word.append(sp)

print("Type in a password to be tested")
print("(start with short passwords (2-4 characters long))")


pas = str(input())
boost = False
trys = 0

print("Starting speedtest... (duration: 10s)")
st = time.time()
while time.time() - st < 10:
    bu(len(pas))
    word = []
    trys = trys + 1
trys = trys / 10    
print("Your computer manages " +str(f"{trys:,}" +" attemps per second."))
print("At this speed you would need up to " + gettime(trys) + " to find the password.") 
print("Would you like to let your computer try to find the password? [Yes/No]")

if "Y" in input().upper():
    trys = 0
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
        
    print("Password found after "+ str(f"{trys:,}") +" trys and " + str(time.time() - st) + " seconds or "+ str((time.time()-st)//60) + " minutes.")






    
    

    