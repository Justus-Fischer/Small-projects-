import time

print("Welcome to the 10 Seconds Game!")
print("Press enter when time is exactly 10.00s")

while True:
    print("Start in 3", end="\r")
    time.sleep(1)
    print("Start in 2", end="\r")
    time.sleep(1)
    print("Start in 1", end="\r")
    time.sleep(1)
    print("GO!                  ", end="\r")
    time.sleep(0.75)
    
    print("")
    st = time.time()
    while True:
        print(str(round(time.time() - st,3)), end="\r")