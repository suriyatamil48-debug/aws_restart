import random
number=random.randint(11,21)
isguessright=False
while isguessright!=True:
    guess=input("guess a number between 11 to 21: ")
    if int(guess)==number:
        print("you guessed {} is correct! you win! ".formate)
        isguessright=True