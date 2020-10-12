"""
Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer)
and validates it to make sure that it is a valid number (look into how credit cards use a checksum).
"""

### welcome message
print('Welcome to credit card validator')


program_start = True

while program_start == True:

    ### luhn

    ### check if there is any space
    credit_card_string = input("what is the credit card number you would like to check")


    ccs = str(credit_card_string)
    finalccs = ""

    for i in range(16):
        if i%2 == 1:
            finalccs += ccs[i]

        elif i%2 == 0:
            if int(ccs[i])*2 >= 10:
                two_digit = str(int(ccs[i])*2)
                sum_two_digit = int(two_digit[0]) + int(two_digit[1])
                finalccs += str(sum_two_digit)

            else:
                finalccs += str(int(ccs[i])*2)

    finalccssum = 0
    for i in range(16):
        finalccssum += int(finalccs[i])

    if finalccssum%10 == 0:
        print("Yes! It's a valid credit card number!")

    else:
        print("No its not a valid credit card number")





    ### continue or not
    continue_play = input("do you want to use the credit card validator again? Y or N")

    if continue_play == "Y" or continue_play == "y":

        program_start = True

    else:

        program_start = False

else:
    print("Thank you for using credit card validator")

