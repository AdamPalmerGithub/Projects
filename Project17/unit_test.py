'''Writing a unit test for project 13, writing unit tests for both functions '''
import unittest #importing unit test

def big_num(lst, n=None):              #functionto find the biggest number in a list
    
    if n is None:    
        n = len(lst) - 1

    if n == 0:         
        return lst[0]
    
    current_big_num = big_num(lst,n-1)  
    if lst[n] > current_big_num:
        return lst[n]
    else:
        return current_big_num

test_list = [1,4,7,4,5,8,3]
biggest_num = big_num(test_list)                              
print(f"The largest number in this list is: {biggest_num}")




def adding_up_to(lst, index):        #function to add items in a list until the desired index
    if index == 0:
        return lst[0]
    else:
        return lst[index] + adding_up_to(lst, index - 1)


input_list = input("Please enter atleast 5 whole numbers seerated by a space: ").split(" ")
user_list_str = [] 
input_index = int(input("How many numbers of list would you like to add?  ")) 
input_py = input_index - 1 

for i in input_list:
    if i.strip(" "):
        user_list_str.append(i)                                    
user_list_int = [int(x) for x in user_list_str]                     


print(f"This is the list you entered: {user_list_int}")  

answer = adding_up_to(user_list_int,input_py)                      
print(f"The sum of numbers to index {input_index} is: {answer}")




class Test_Big_Num(unittest.TestCase):                #tests big_num function, 1st if it works and 2nd how it works with multiple numbers
    def test_find_big_num(self):
        self.assertEqual(big_num([1, 2, 3, 4, 5]), 5)

    def test_big_num_fringe(self):
        self.assertEqual(big_num([1,2,3,3,3]), 3)



class Test_adding_up_to(unittest.TestCase):     #tests the adding ip function
    def test_single_element(self):
        self.assertEqual(adding_up_to([42], 0), 42)    #tests with one item

    def test_adding_up_to_10(self):
        self.assertEqual(adding_up_to([1,2,3,4,5,6], 3),10)  #more than one item

    def test_adding_up_to_negative_10(self):
        self.assertEqual(adding_up_to([-1,-2,-3,-4,-5,-6],3),-10)   #with negitive numbers

    def test_empty_list(self):
        with self.assertRaises(IndexError):    #if it fails with no list given
            adding_up_to([], 0)

if __name__ == '__main__':
    unittest.main()