"""
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""


## welcome message
print("Welcome to the Prime factor finder!")

program_play = True

while program_play == True:

    ## number input
    number_input = int(input("Please enter a number between 1 to 1000000"))

    ### main function for prime factor

    ### find all the lcm
    lcm = []

    for n in range(1,number_input):
        if number_input%n == 0:
            for i in range(1,n):
                if n%i == 0:
                    if n in lcm:
                        pass
                    else:
                        lcm.append(n)
                else:
                    pass
        else:
            pass
    ### filter out all non prime numbers

    prime_number = []


    for all_lcm in lcm:

        checker = []

        for n in range(1, all_lcm):
            if all_lcm % n == 0:
                for i in range(1, n):
                    if n % i == 0:
                        if n in checker:
                            pass
                        else:
                            checker.append(n)
                    else:
                        pass
            else:
                pass

        if checker == []:
            prime_number.append(all_lcm)

        else:
            pass



    ## result output
    print(prime_number)
    continue_play = input("do you want to use the Prime factor finder again? Y or N")


    ###continue to use the program or not
    if continue_play == "Y" or continue_play == "y":

        program_play = True

    else:

        program_play = False

else:
    print("Thank you for using Prime factor finder")
