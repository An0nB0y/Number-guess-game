
import random

stage = 1
high_num = 10
win = False
turns =0
high_num += high_num

while win==False:
    your_guess = input(" \n Enter a number between 1 and %d : \t" % (high_num))
    turns +=1
    if random_number==int(your_guess):
        print("You won!")
        if turns == 1:

            print ("\n WOW! You guessed the number from the first time. U are very lucky O_o \n")
        elif turns == 2:
            print ("\n Good, U are not that lucky but u are clever :D \n")
        else:
            print(" \n Hey, u are almost lost. But, u catch up ur brain at the end. Stay focused next time.\n")
            print 'Turns:', turns
        win == True
        stage += 1
        random_number = random.randint(1, high_num)
        print ("You are now passing to the next stage. It's going to be quite harder. GoodLuck :D \n \n \n \n \n")
        print ("*********************************************** STAGE %d *********************************************** \n " % (stage) )
    else:
     if random_number>int(your_guess):
        print("Your Guess was low, Please enter a higher number")
     else:
        print("Your guess was high, please enter a lower number")
