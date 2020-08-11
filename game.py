
#Import 
import random

# Variables
high_num = 10
random_number = random.randint(1,high_num)
win = False
turns = 0
score = 0

#Level1
def level1():
    
    global random_number
    global turns
    global high_num
    global score 

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("WOW! You get it from the first time. You are very lucky 0 o 0")
                score += 3
            if turns == 2:
                print("Good, You are not that lucky but u are clever.")
                score += 2

            else:
                print("Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time")
                score += 1
                print("Number of turns you have used: ",turns)
            turns =0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")


#Level2
def level2():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("WOW! You get it from the first time. You are very lucky 0 o 0")
                score += 4
            if turns == 2:
                print("Good, You are not that lucky but u are clever.")
                score += 3

            else:
                print("Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time")
                print("Number of turns you have used: ",turns)
                score += 2

            win == True
            turns =0
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")


#Level3
def level3():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 5
            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 4

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 3
                print("Number of turns you have used: ",turns)
            turns = 0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")

#Level4
def level4():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 6
            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 5

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 4
                print("Number of turns you have used: ",turns)
            turns = 0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")

#Level5
def level5():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 7
            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 6

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 5
                print("Number of turns you have used: ",turns)
            turns = 0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")


#Level6
def level6():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score +=  8
            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 7

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 6
                print("Number of turns you have used: ",turns)

            turns = 0 
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")

#Level7
def level7():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 9

            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 8

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 7
                print("Number of turns you have used: ",turns)
            
            turns = 0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")


#Level8
def level8():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 10
            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 9

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 8
                print("Number of turns you have used: ",turns)

            turns = 0    
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")

#Level9
def level9():
    global random_number
    global turns
    global high_num
    global score 

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 11

            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 10 

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 9
                print("Number of turns you have used: ",turns)

            turns = 0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("your guess was high, please enter a lower number")


#Level10
def level10():
    global random_number
    global turns
    global high_num
    global score

    high_num += high_num
    random_number = random.randint(1,high_num)

    while win==False:
        your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
        turns +=1

        if random_number==int(your_guess):

            if turns == 1:
                print("\n WOW! You get it from the first time. You are very lucky 0 o 0 \n")
                score += 20

            if turns == 2:
                print("\n Good, You are not that lucky but u are clever.\n")
                score += 15

            else:
                print("\n Hey, u are almost lost the road. But, you catch up your brain at the end. Stay focused next time\n")
                score += 10
                print("Number of turns you have used: ",turns)

            turns = 0
            win == True
            break
        else:
         if random_number>int(your_guess):
            print("Your Guess was low, Please enter a higher number")
         else:
            print("Your guess was high, please enter a lower number")



#Main
def main():
    
    print ("\n \n \n \n ********************************************************* STAGE 1 ********************************************************* \n \n \n \n")
    level1()
    print ("\n Your score is: %d \n" % (score))

    
    print ("\n \n \n \n ********************************************************* STAGE 2 ********************************************************* \n \n \n \n")
    level2()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 3 ********************************************************* \n \n \n \n")
    level3()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 4 ********************************************************* \n \n \n \n")
    level4()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 5 ********************************************************* \n \n \n \n")
    level5()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 6 ********************************************************* \n \n \n \n")
    level6()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 7 ********************************************************* \n \n \n \n")
    level7()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 8 ********************************************************* \n \n \n \n")
    level8()
    print ("\n Your score is: %d \n" % (score))
    
    print ("\n \n \n \n ********************************************************* STAGE 9 ********************************************************* \n \n \n \n")
    level9()
    print ("\n Your score is: %d \n" % (score)) 

    print ("\n \n \n \n ********************************************************* FINAL STAGE  ********************************************************* \n \n \n \n")
    level10()

    print ("\n Your final score is: %d " % (score))

main()
