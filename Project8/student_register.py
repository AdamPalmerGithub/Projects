'''This program takes an input for the number of students.
Then it opens a new text file and allows the user to write
the student ID's with signiture space for the number inputted,
finally closing the file again. '''

num_stu = int(input("How many students are registering?"))   #Input for the number of students entering
with open("reg_form.txt", "w+") as file:                   #Creating a net text file for writing
    file.write("List of student ID's for the exam.")         #Titleing the list withj file.write
    for i in range(num_stu):                                 #For loop equal to the number of students
        Stu_id = (input("please enter the student id. ") + "........")  #Student id inpt and ... for signing 
        file.write("\n" + Stu_id)                            #adding the input to the list and restarting the loop
    file.close()                                             #Closing the file
              