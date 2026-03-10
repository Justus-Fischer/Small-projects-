print("Welcome to the WordSkyscraper")
print("What's your Word?")
text = str(input())
print(str("Ok What should be the height of your " + text + "-Building?"))
height = int(input()) # height of the Roof -> Building is 2.5 times as high
print("Last Question: Should the building be vertical? [Yes/No]")
d = str(input())
if "y" in d or "Y" in d:
    vertical = True # Vertical or Horizontal?
else:
    vertical = False
    



ftext = str(text + " ")

if vertical == False:
    number = int(0)
    for i in range (height):
        print(ftext * number)
        number = number + 1
    
    for i in range (height):
        print(ftext * number)
        number = number - 1
        
        
else:
    length = len(ftext)
    number = height
    br = int(1)
    for i in range(height):
        print(" " * length * number + ftext * br)
        number = number - 1
        br = br + 2
    for i in range(height + height // 2):
        print(" " * length * number + ftext * br)
        
    

