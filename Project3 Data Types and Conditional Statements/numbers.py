threeNumbers = int(input("Enter three integers: "))
print(threeNumbers)
#Asks the user to input three integers


def add(a,b,c):
    return a+b+c
#defines the add function



srt_num = str(threeNumbers)
num1 = int(srt_num[0])
num2 = int(srt_num[1])
num3 = int(srt_num[2])
#splits the number into its ndividial componants

num_a = add(num1,num2,num3)
print(num_a)
#use the function to add all the numbers together.

def minus(a,b):
    return a-b
#function for minusing one number from another

num_b = minus(num1,num2)
print(num_b)
#the first number minus the second

def multi(a,b):
    return a*b
#function for multiplying two values

def divi(a,b):
    return(a/b)
#function to divide two values

num_c = multi(num3,num1)
print(num_c)
#third number multiplyed by the first

num_d = divi(num_a,num3)
print(num_d)
#sum of all three numbers divided by the third