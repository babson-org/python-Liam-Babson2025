secret = ("7")
while True:
    guess =input("enter your guess")
    if guess == secret:
        print("you got it")
        break
    else:
        print("try again")