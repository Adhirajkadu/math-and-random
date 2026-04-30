import random
    
number =random.randint(0, 20)
chances= 0
print("Guess passsword between 0000-1234, you only have 3 chance\n")

while chances < 3:
    guess=int(input("Guess your password :"))

    if guess == number:
        print("YOU Opened the mobile !!!")
        break
    elif guess > number:
        print("Your guess is too high, try lower number")
    else:
        print("Your guess is too low, try higher number")
    chances += 1
if not chances < 3:
    print("YOU Didn't Open the mobile!!! the number is ",number)