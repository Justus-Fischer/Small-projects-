import random

worter = ["CAR", "TREE", "HOUSE"]
wor = random.choice(worter)
liwor = list(wor)
suc = ["_ "] * len(wor)
print(wor)
print("Welcome to the hangman game. What is your first guess (tip in one letter)")
fer = False

while fer == False:
    guess = str(input().upper())
    if guess in wor:
        for i in range(len(wor)):
            if liwor[i] == guess:
                suc[i] = str(guess)
            
        print(" ".join(suc))
        if not "_" in " ".join(suc):
            fer = True
        continue
            
    print(" ".join(suc))
    
print("Congratulations!")