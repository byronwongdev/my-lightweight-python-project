'''
Sorting - Implement one type of sorting algorithms: bubble sort
'''

### bubble sort

inputlist = list(input("any combinations of random characters and numbers that you would like to sort"))


sort_count = 0
finish_count = 0
finish = False

while finish != True:
    
    loop_count = 0

    for n in range(1,len(inputlist)):

        

        if inputlist[n-1] > inputlist[n]:

            temp_number = inputlist[n-1]
            inputlist[n-1] = inputlist[n]
            inputlist[n] = temp_number


            sort_count += 1
            print(inputlist)
            print(sort_count)
        
        else:
            loop_count += 1

            if loop_count == len(inputlist)-1:

                finish = True
            else:
                pass
    

print("it is finished")




            