str_manip = input(str("Enter a sentence here "))
#Gets the user to input a sentence

sentence_length = str(len(str_manip))
print("The sentence is " + sentence_length + " characters long. ")
#Tells the user the lenth of the sentence

last_letter = (str_manip[-1])
print("The last letter of the sentence is " + last_letter + ".")
#Tells the user the last letter of the sentence

str_manip_replace = str_manip.replace(last_letter,"@")
print(str_manip_replace)
#Replaces all instances of the last letter with "@"

str_manip_back3 = (str_manip[-1:-4:-1])
print(str_manip[-1:-4:-1])
#Tells the user the last 3 characters backwards

str_manip_combo = (str_manip[0:3]) + (str_manip[-2:])
print(str_manip_combo)
#Tells the user a word made of the first 3 letters and last two