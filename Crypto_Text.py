import random
int key
int VZ

def genKey():
    if random.randint(1, 0) == 1:
        VZ = 1
    else:
        VZ = 0
        
    key = andom.randint(1, 50)
    if VZ == 0:
        key = 0 - key
print("Welcome to Crypto_Text!")

while True:
    print("Do you want to Encrypt or Decrypt? (En/De)")
    if "EN" in input().upper():
        print("Choose your key (every number possible) or type generate for a key which is saver")
        try:
            key = int(input())
        except:
            key = genKey()
            
        
        
    else: