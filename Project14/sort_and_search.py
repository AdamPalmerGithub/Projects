array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

#It would be best to use a linear search, we know what we are looking for and the list isn't in order

def linear_search(item, arr):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
lin_answer = linear_search(9, array)                                #I think this was the correct choice as the data was disorganized, but
print(f"The item you are looking for is at index: {lin_answer}")                      #small enough where performance won't be affected.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j =i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = key

in_sort = insertion_sort(array)
print(f"The array after the insertion sort:\n{array}")

def binary_search(item, arr):
    low, high = 0, len(arr) - 1
    while high >= low:
        mid = (low + high) //2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

bin_answer = binary_search(9, array)
print(f"The item you are looking for is at index: {bin_answer}")
#A binary search would be used on data that has been sorted for a quick and efficient answer
#Examples would be: file systems, games, databases and libraries
