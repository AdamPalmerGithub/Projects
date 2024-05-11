'''This program opens a file and saves the contents as a variable before closing it, splits the file 
by each line, and for each value spits it into names and dates using the spaces, then returns it to the user'''



file = open("Project8\\DOB.txt", "r")
file_line = file.read()
file.close

file_lst = file_line.split("\n")

names = []
birthdays = []

print("This is a list of the names: ")


for i in file_lst:
    
    names = i.split(" ")[0:2]

    print(names)

print("This is a list of the birthdays: ")

for i in file_lst:

    birthdays = i.split(" ")[2:5]

    print(birthdays) 





