"""
Have the program find prime numbers until the user chooses to stop asking for the next one.
"""


### welcome message

print("Welcome to next prime number generator !")


### the generator
prime_number_list = []

program_start = True

test_number = 1

while test_number < 1000000:
    test_number += 1

    for i in range(2,test_number):
        if (test_number%i) == 0:
            break

    else:
        print("Congratulations you have found a new prime number" + str(test_number))
        prime_number_list.append(test_number)


print("Thank you for using the next prime number generator! Have a great day!")