'''Using merge sort provided, editing it to use string length and testing it on lists'''

def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1
    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2
    return items

def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if len(items[i_1]) > len(items[i_2]):             #adding len to get the length of the strings
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else:  
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1
        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
                i_t += 1
        else:  
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1

    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]

#by adding len on line 22 this will sort by string length

sports = ["football", "soccer", "basketball", "tennis", "golf", "volleyball", "cricket", "rugby", "baseball", "hockey"]
furniture = ["chair", "table", "sofa", "lamp", "bookshelf", "rug", "desk", "ottoman", "couch", "stool"]
space = ["sun", "moon", "stars", "planet", "galaxy", "comet", "nebula", "asteroid", "satellite", "meteor"]

merged_sports = merge_sort(sports)        #calling the merge function
merged_furniture = merge_sort(furniture)
merged_space = merge_sort(space)

print(f"sorted lists by their length:\n{merged_sports}\n{merged_furniture}\n{merged_space}")