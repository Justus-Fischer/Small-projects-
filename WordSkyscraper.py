text = "YourText"
height = 10 # height of the Building



ftext = str(text + " ")
number = int(0)

for i in range (height):
    print(ftext * number)
    number = number + 1
    
for i in range (height):
    print(ftext * number)
    number = number - 1

