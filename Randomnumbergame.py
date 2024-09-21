def randomgame ():
    import random
    import sys
    i=0
    counter1=2
    a=random.randint(20,30)
    print("Rules: I will guess a random number. You have three chances to guess it right. One clue will appear after each chance. Lets play!")
    while i <=2:
        num=int(input("Enter the number you are guessing: "))
        if num < a:
            print("My number is greater.", end=" ")
            if counter1 !=0:
                print("Try a bigger number.", end=" ")
            print("You have", counter1, "chances left")
        elif num >a:
            print("My number is lesser.", end=" ")
            if counter1 !=0:
                print("Try a smaller number.", end=" ")
            print("You have", counter1, "chances left")
        else:
            print("Yay!You won the game!! My number was indeed", a)
            sys.exit()
        if counter1 == 2:
            print("Clue 1: My number is somewhere between 10 and 40 ")
        if counter1 == 1:
            print("Clue 2: My number is definitely between 20 and 30 ")
        i += 1
        counter1 -= 1
    print("You lose. The number was", a)
    print( "Better luck next time!")
randomgame ()