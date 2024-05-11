# # with open('Project4\userInput.txt', 'w') as file:
# #    file.write("")
# # close() as file 
# #file.write(int("userimput"))


# userList = int(input("please enter a list of numbers, one at a time and finish with '-1' :"))

# while userList != -1: 
#     print("input the next number or finish with '-1' ")
#     userList = int(input("please enter a list of numbers, one at a time and finish with '-1' :"))
# if 
    
     
# I tried to store the numbers in a blank txt file. clearing it on start of program and would add each value as it went
# I then remembered the tutorial video lol
 

total = 0
loops = 0
#blank values to add with as the program goes.

userInput = int(input("enter a number, use -1 to break : "))
#the first input
while userInput != -1:          # repeats aslong as the entered value isnt -1
    total += userInput

    loops += 1
#updates the total and loop value on each repeat
    print(loops)

    userInput = int(input("enter a number, use -1 to break : "))

    if userInput == -1:
        #print("The total of all inputted numbers is " + total)
        break
#stops the program when -1 is detected
    
averageInput = total / loops
print("The total of all inputted numbers is: "+ str(total))
print("The average inputted number is: " + str(averageInput))
#works out the average input by the user

