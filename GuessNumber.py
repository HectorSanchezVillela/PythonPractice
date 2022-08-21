import random
import discord
def run():
    x=random.randint(1,99)
    n=int(input("!!!Guess the number! (1 to 99): "))
    while n!=x:
        if n>x:
            n=int(input("Too High! Aim lower: "))
        else:
            n=int(input("Too Low! Aim higher: "))
    print("You guessed it! The number is: "+str(x))



if __name__ == '__main__':
    run()