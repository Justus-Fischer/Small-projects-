import random

worter = ["CAR", "TREE", "HOUSE", "QUIZZICAL", "XYLOPHONE",
    "SPHINX", "JAZZ", "VORTEX", "KALEIDOSCOPE", "WALTZ", "EPIPHANY", "KNOT", "WHIMSICAL",
          "CAT","SUN","DOG","HAT","SKY","BALL","BOOK","TOY","MAN"]

wor = random.choice(worter)
liwor = list(wor)
suc = ["_ "] * len(wor)
fehl = 0

while True:
    
    print("Welcome to the hangman game. What is your first guess (tip in one letter)")
    fer = False
    print(" ".join(suc))
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
        if not guess in wor:
            fehl = fehl + 1
        print(" ".join(suc))
    
    print("Congratulations!")
    print("You had " + str(fehl) + " failed attemps.")
    print("Start next round with [YES] or quit with [NO]")
    guess = str(input().upper())
    if "N" in guess:
        break
    
    wor = random.choice(worter)
    liwor = list(wor)
    suc = ["_ "] * len(wor)
    fehl = 0