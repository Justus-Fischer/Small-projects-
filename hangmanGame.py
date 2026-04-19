import random


wordseasy  = ["CAT", "DOG", "BOOK", "TREE","FISH","HAT","CITY","SUN","BALL"
                "RAT","CAR","PEN","MOON","FARM","BIRD","HOUSE","JAZZ","KNOT"
                  "SUN","SKY","TOY","MAN" ]

wordshard = ["QWERTZ","QUIZZICAL", "XYLOPHONE", "SPHINX", "VORTEX", "KALEIDOSCOPE",
                 "WALTZ", "EPIPHANY" "WHIMSICAL","EXQUISITE","JAZZILY","PSYCHOLOGY",
                    "BUNGALOWS","IMMISCIBLE","ARCHAIC","VORTICITY","GAUCHE","ZEALOUS",
                        "UNDEFEATED","PHENOMENON"]

print("Choose your difficulty level [easy/hard]")
if "RD" in input().upper():
    wor = random.choice(wordshard) 
else:
    wor = random.choice(wordseasy)
liwor = list(wor)
suc = ["_ "] * len(wor)
fehl = 0

while True:
    
    print("Welcome to the hangman game. What is your first guess (tip in one letter)")
    fer = False
    print(" ".join(suc), end="\r")
    print(" ")
    while fer == False:
        guess = str(input().upper())
        if guess in wor:
            for i in range(len(wor)):
                if liwor[i] == guess:
                    suc[i] = str(guess)
            
            print(" ".join(suc) + " (" + guess + ")", end="\r")
            print(" ")
            if not "_" in " ".join(suc):
                fer = True
            continue
        if not guess in wor:
            fehl = fehl + 1
        print(" ".join(suc) + " (" + guess + ")", end="\r")
    
    print("Congratulations!")
    print("You had " + str(fehl) + " failed attemps.")
    print("Start next round with [YES] or quit with [NO]")
    guess = str(input().upper())
    if "N" in guess:
        break
    print("Choose your difficulty level [easy/hard]")
    if "RD" in  input().upper():
        wor = random.choice(wordshard) 
    else:
        wor = random.choice(wordseasy)
    
    liwor = list(wor)
    suc = ["_ "] * len(wor)
    fehl = 0