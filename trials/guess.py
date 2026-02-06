import random

print("Welcome to number guessing game.")
dif=input("Choose difficulty 'easy' or 'hard':").lower()
r=random.randint(1,100)
guess=0
n=0
if(dif=='easy'):
    n=10
else:
    n=5
while(n>0):
    print(f"You have {n} attempts to guess the correct number")
    guess=int(input("Enter your guess between 1 and 100:"))
    if(r==guess):
        print("You guessed the correct number")
        break
    elif(guess<r):
        print("Too Low!")
        n-=1
    else:
        print("Too High!")
        n-=1
    