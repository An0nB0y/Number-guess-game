#Import
import random
#Variables
high_num = 10
random_number = random.randint(1,high_num)
win = False
turns = 0
stage = 1

#Stage 1
def stage1():
	while win==False:
    	your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
    	turns +=1
    	if random_number==int(your_guess):
        	print("You won!")
        	if turns == 1:

            	print ("WOW! You guessed the number from the first time. U are very lucky O_o \n")
        	elif turns == 2:
            	print ("Good, U are not that lucky but u are clever :D")
       		else:
            	print("Hey, u are almost lost. But, u catch up ur brain at the end. Stay focused next time. \n")
            	print ('Turns:', turns)
        	high_num +=high_num
        	print ("You are now passing to the next stage. It's going to be quite harder. GoodLuck :D")
        	win == True
        	stage +=1        
    	else:
     		if random_number>int(your_guess):
        	print("Your Guess was low, Please enter a higher number")
     	else:
        	print("Your guess was high, please enter a lower number")

#Stage 2
def stage2():
	while win == True:	
		win = False
		while win==False:
    		your_guess = input("Enter a number between 1 and %d : \t" % (high_num))
    		turns +=1
    		if random_number==int(your_guess):
        		print("You won!\n")
        		if turns == 1:

            		print ("WOW! You guessed the number from the first time. U are very lucky O_o \n")
        		elif turns == 2:
            		print ("Good, U are not that lucky but u are clever :D \n")
        		else:
            		print("Hey, u are almost lost. But, u catch up ur brain at the end. Stay focused next time.")
            		print ('Turns:', turns)
        	high_num += high_num
        	print ("You are now passing to the next stage. It's going to be quite harder. GoodLuck :D")
        	win == True
        	break
        
    		else:
     			if random_number>int(your_guess):
        			print("Your Guess was low, Please enter a higher number")
     			else:
       				print("Your guess was high, please enter a lower number")
stage2()

#Level Up
if stage == 1:
	stage1()
elif stage == 2:
	stage2()
