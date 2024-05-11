# try:
#     statement  run as normal part of program

# except:
#     statement
# else:
#     statement

# finally:
#     statement

#with open('filename.txt, 'r') as file:          ('r' means read file)
    #content = file.read()

#file = open('file.txt', 'r')
#content = file.read()
#file.close()

#raise keyword to specify exception
#num = int(input("enter value"))
#if num < 10:
#    raise exception(f'')

#example 1
def validate_input(value):
    if not isinstance(value, int):
      raise ValueError("input must be an integer")
    
try:
   validate_input("hello")
except ValueError as e:
   print(f"error: {e}")
   

#example 2
#print(true + true)   boolean can be unteger 1 + 1 = 2

# enter either in or float
#                      true              and             true
#                       (     entire statement is true         )
#  true                 (             false                    )
#if not true do thie           v
def add_num(num1,num2):
    if not ( isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
       raise ValueError("both values should be in or float")
    return num1 + num2

print(add_num(26, 10))    #should work

#print(add_num(23, "10"))

