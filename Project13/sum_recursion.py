'''A program to get a list and index from the user then add values from the list together until reaching the index requested.
This uses recursion rather than loops'''


def adding_up_to(lst, index):
    if index == 0:          #if the index is 0 then it returns the first item, base case. 
        return lst[0]
    else:
        return lst[index] + adding_up_to(lst, index - 1)      #adds current index to the previous index totals, recursive case.


input_list = input("Please enter atleast 5 whole numbers seerated by a space: ").split(" ")       #takes the user input, filter out extra spaces, to the empty list
user_list_str = [] 
input_index = int(input("How many numbers of list would you like to add?  "))                      #user inputs how many values from the list they want to add 
input_py = input_index - 1                                                                         # minus 1 as python starts from 0 not 1

for i in input_list:
    if i.strip(" "):
        user_list_str.append(i)                                          #removes the extra spaces from the list
user_list_int = [int(x) for x in user_list_str]                          # makes each value in the list a int from a str


print(f"This is the list you entered: {user_list_int}")  

answer = adding_up_to(user_list_int,input_py)                            #calls the function 
print(f"The sum of numbers to index {input_index} is: {answer}")


