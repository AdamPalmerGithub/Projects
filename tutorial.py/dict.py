my_dict = {
    "brand": "VW",
    "model": "polo",
    "year": 2018,
    "year": 2024              #goes to most final one takes 2024
}
#print(my_dict)
#print(my_dict["model"])
x = my_dict.get("model")          #both get the same end value
#print(x)

#print(my_dict.items())

#to check if a specific key is persent in the dict
#if "model" in my_dict:
    #print("yes, 'model' in one of the keys in the dictionaries")

#my_dict.update({"year":1999})
#print(my_dict)

#my_dict.pop("model")
#print(my_dict)

# del my_dict["year"]
# #print(my_dict)

# car_dictionary = my_dict.copy()
# car_dictionary = dict(my_dict)

child1 = dict(name="adam,age=8")
child2 = dict(name="ben",age=10)
child3 = {"name":"charlize","age":7}

class_list = {"child1":child1,"child2":child2,"child3":child3}

print(class_list)

print(class_list["child2"]["name"])
