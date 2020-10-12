"""
Collatz Conjecture - Start with a number n > 1. 
Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""

## welcome message

print("Welcome to collatz conjecture number step finder")

## number input
program_play = True

while program_play == True:

    steplist = []

    test_number = int(input("the number you would like to test"))
    step_counter = 0

    while test_number != 1:
        steplist.append(int(test_number))
        step_counter += 1

        if test_number%2 != 0:
            test_number = test_number*3 + 1


        elif test_number%2 == 0:
            test_number = test_number/2
        
        
    steplist.append(1)

    print(steplist)

    print("the total step is " + str(step_counter))

    ###continue to use the program or not
    continue_play = input("do you want to use the collatz conjecture number step finder again? Y or N")
    if continue_play == "Y" or continue_play == "y":

        program_play = True

    else:

        program_play = False

print("Thank you for using collatz conjecture number step finder!")
