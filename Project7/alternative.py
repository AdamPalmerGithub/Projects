'''This program will take an input from the user, set the unput to lower case, then for each value in the string capital
or lower case it depending if its odd or even for the length of the lower_string  '''
string = input("Please enter a word or phrase: ")
lower_string = string.lower()       # sets the string to lower case
StRiNg = ""                         # Empty string for new variable


# def cap_letters():
for i in range(len(lower_string)):  #i is a place holder and changes for each value in the lencth fo the string 
    if i % 2 == 0:                            #check to see if the value is odd or even
        StRiNg += lower_string[i].upper()     # for each odd value it makes that letter upper and adds it to the new string
    else:                                     # for each even value makes it lower and adds it to the new string
        StRiNg += lower_string[i].lower()

print(StRiNg)   #returns the new string


# lower_string = input("Please enter a word or phrase: ")       #wrote it as a function moving the empty variable into the def
                    
# def cap_letters(x):
#     StRiNg = ""
#     for i in range(len(x)): 
#         if i % 2 == 0:                           
#             StRiNg += x[i].upper()     
#         else:                                     
#             StRiNg += x[i].lower()
#     return StRiNg

# print(cap_letters(lower_string))   

'''This function uses a for loop, for each item in lst_string (x) it checks if its odd or even making it caps or not.
it returns it as a list which is printed with a join to get a sentance. '''

lst_str = string.split(' ')    #input as a list for each word

string_cap = []  #an empty place holder for a list
for x in lst_str: #x is a place holder to check each value in the list
    if i % 2 == 0: #checks for odd or even, ie each other value in a list
        string_cap.append(x.upper())   #makes the item x in list caps
    else:
        string_cap.append(x)  #if not ignores it
    i = int(not i)

print(" ".join(string_cap))  #returns it as a string connected with ' '
