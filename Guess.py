import random
    
number =random.randint(0, 20)
chances= 0
print("Guess a number between 0-20, you only have 3 chance\n")

while chances < 3:
    guess=int(input("Guess your number :"))

    if guess == number:
        print("YOU WIN!!!")
        break
    elif guess > number:
        print("Your guess is too high, try lower number")
    else:
        print("Your guess is too low, try higher number")
    chances += 1
if not chances < 3:
    print("YOU LOSE!!! the number is ",number)