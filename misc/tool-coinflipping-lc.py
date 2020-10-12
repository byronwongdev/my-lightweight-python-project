"""
Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. 
The code should record the outcomes and count the number of tails and heads.
"""

## we are using random library in this programme
import random 

## welcome message

print("Welcome to coin flip simulation")

## number input
program_play = True

while program_play == True:

    number_input = int(input("how many times do you want to flip the coin?"))
    result_list = []

    for n in range(1,number_input+1):
        random_number = random.randint(0,1)
        result_list.append(str(random_number))

    print("tail :" + str(result_list.count('1')))
    print("head :" + str(result_list.count('0')))
    ## programme

    ###continue to use the program or not
    continue_play = input("do you want to use the coinflip simulation again? Y or N")
    if continue_play == "Y" or continue_play == "y":

        program_play = True

    else:

        program_play = False

print("Thank you for using coinflip simulation!")



