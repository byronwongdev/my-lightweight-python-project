"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""


## welcome message
print("Welcome to the Fibonacci Generator!")

program_play = True

while program_play == True:

    ## number input
    number_input = int(input("Please enter a number between 1 to 1000"))

    ### main function for Fibonacci

    if number_input > 1:

        fib_result = [1,1]
        for i in range(number_input-2):
            fib_result.append(fib_result[i]+fib_result[i+1])
            print(fib_result[i]+fib_result[i+1])

    elif number_input == 1:

        fib_result = [1]

    ## result output
    print(fib_result)
    continue_play = input("do you want to use the fibonacci generator again? Y or N")


    ###continue to use the program or not
    if continue_play == "Y" or continue_play == "y":

        program_play = True

    else:

        program_play = False

else:
    print("Thank you for using fibonacci generator creator ")



