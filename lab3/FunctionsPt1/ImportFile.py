def akzholGame():
    print ("The number is between 1 to 100\nTake a gues: ")
    while True:
        a = int(input())
        if a == 77:
            print("You have won!")
            break
        else:
            print ("Try it again")

akzholGame()