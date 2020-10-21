"""
linear-search 
when you run this in terminal, it will show the step of searching a particular character within a string given by a user
"""

def linear_search(s,c):
    step = 0
    for a in range(len(s)):
        if s[a] == c:
            step += 1
            print("the character ' "+ str(s[a])+ " ' has been found in position" + str(step))
            break

        else:
            step += 1
            print("the character ' "+ str(s[a])+ " ' is not character '" + str(c) +" ', current step:" + str(step))
            


string_user_input = str(input("please enter a string:"))
char_user_input = str(input("please enter a character that you would like to search:"))

linear_search(string_user_input,char_user_input)