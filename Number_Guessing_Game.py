# In this game, the player has 7 lives. They are required to guess the number within 7 tries. 
# Otherwise, the game is lost.
import random

low_n=int(input("Enter the lowest bound: "))
high_n=int(input("Enter the highest bound: "))

realnumber=random.randint(low_n,high_n)

life=7
print(f"Your life is: {life}")

while life>0:
    guess=int(input("Enter your guess: "))
    if guess==realnumber:
        print("You won.")
        break
    elif guess>realnumber:
        print("The number is too high.Please try a lower number.")
    else:
        print("The number is too lower.Please try a higher number.")
    life=life-1
    print(f"Your life is: {life}")
if life==0:
    print("You lost the game.")
    print(f"The guessed number is: {realnumber}")