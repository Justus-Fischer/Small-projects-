text = "YourText"
height = 6 # height of the Roof -> Building is 2.5 times as high
vertical = True # Vertical or Horizontal?



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
        
    

