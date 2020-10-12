"""
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places.
Keep a limit to how far the program will go.
"""

## welcome message
print("Welcome to the Math pi Generator!")

program_play = True

while program_play == True:

    ## number input
    number_input = int(input("Please enter a number between 1 to 10 for dp"))


    pi_b = 3
    for i in range(1000000):
        pi_b += (4/((2+i*4)*(3+i*4)*(4+i*4)) - 4/((4+i*4)*(5+i*4)*(6+i*4)))

    ## result output
    print(round(pi_b,number_input))

    ###continue to use the program or not
    continue_play = input("do you want to use the Pi generator again? Y or N")
    if continue_play == "Y" or continue_play == "y":

        program_play = True

    else:

        program_play = False

else:
    print("Thank you for using pi generator creator !")







