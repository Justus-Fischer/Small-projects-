import random


def genKey():
    if random.randint(0, 1) > 0.5:
        VZ = 1
    else:
        VZ = 0
        
    key = random.randint(1, 500)
    if VZ == 0:
        key = 0 - key
        
    return key



def crypto(mes,mode):
    if mode == 1:
        bmes = list(mes)
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            bmes[i] = chr(bmes[i] + key)
    else:
        bmes = list(mes)
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            bmes[i] = chr(bmes[i] - key)
    return "".join(bmes)
            

    
print("Welcome to Crypto_Text!")  


while True:
    print("Do you want to Encrypt or Decrypt? (En/De)")
    if "EN" in input().upper():
        print('Choose your key (a number bigger than 0) or type "generate" for a key which is saver')
        sp = input()
        if "GEN" in sp.upper():
            key = genKey()
        else:
            key = int(sp)
            
            
        print("Type in the message that should be encrypted")
        mes = str(input())
        
        print("Your encrypted message is: ")
        print(" ")
        print(str(crypto(mes,1)))
        print(" ")
        print("Please don't forget your Key: " + str(key))
            
        
        
    else:
        print("Type in/Paste the encrypted message")
        mes = str(input())
        print("Type in the Key")
        key = int(input())
        print(" ")
        print("The decrypted message is: ")
        print(" ")
        print(str(crypto(mes,2)))
        print(" ")