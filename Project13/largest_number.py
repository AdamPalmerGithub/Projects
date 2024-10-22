'''A program to find the largest number in a list using reccursion'''


def big_num(lst, n=None):

    if n is None:  # sets n to the last item in the list to work its way back
        n = len(lst) - 1

    if n == 0:  # base case to return the first element
        return lst[0]
    current_big_num = big_num(lst, n-1)
# recursive case, checks to find the maximum value
    if lst[n] > current_big_num:
        return lst[n]
    else:
        return current_big_num


test_list = [1, 4, 7, 4, 5, 8, 3]
biggest_num = big_num(test_list)  # call the function
print(f"The largest number in this list is: {biggest_num}")
