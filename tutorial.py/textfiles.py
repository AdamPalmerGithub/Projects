#example 1

#reletive path - tutorial.py\list_of_cats.txt
#absolute path - D:\CoGrammer bootcamp Python\Projects\tutorial.py\list_of_cats.txt

#traditional method (explicit)
#file = open("tutorial.py\list_of_cats.txt", 'r')

# #newer implicit
# with open('tutorial.py\list_of_cats.txt', 'r') as x:
#     print(x)

#     content = x.read()
#     print(content)
    

#Read from a file python 1. read() 2. readline() 3. readlines()
    
# with open('tutorial.py\list_of_cats.txt', 'w') as file:
#     #print(x)

#     file.write("\ncattie")

#close file(x)

#read then overwrites the file

with open('tutorial.py\list_of_cats.txt', 'a') as file:
    #print(x)

    file.write("\ncattie")  

#adds it to the list
    
#file.seek(0) once python  read a file, use seek to reset the 'curser' to the top for multiple reads
    

    

