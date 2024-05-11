list = ["dav", "dev", "dov"]
boolean = True
string = "hello world"

# print(type(list))
# print(type(boolean))
# print(type(string))

def this_is_a_function(a, b):
    return a*b 

print(type(this_is_a_function))

class Student():
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades

    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        print("The average for student " + self.name + " is " + str(average))

ben = Student(20, "Ben Dover", "Male", [64,65])
anita = Student(19, "Anita Pea", "Female", [82,58])

anita.compute_average()
print(ben.name)