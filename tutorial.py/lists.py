# fruits = ['apple', 'banana', 'orange']
# fruits.extend(['grape', 'pineapple'])
# #print(fruits)
# #print(len(fruits))

# fruits.insert(3, 'blueberry')
# fruits[1:3] = ['kiwi', 'strawberry']
# #print(fruits)

# fruits_tuple = ("cherry", "granadilla")
# fruits.extend(fruits_tuple)
# #print(fruits)

# #print(type(fruits), type(fruits_tuple))

# #removing
# removed_item = fruits.pop(2)
# #print(removed_item)

# fruits.remove("cherry")
# #print(fruits)

# del fruits[0]
# #print(fruits)

# #fruits.clear()

# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)

#looping

fruits1 = ['apple', 'banana', 'orange']

for x in fruits1:
    print(x)
for i in range(len(fruits1)):
    print(fruits1[i])

    i = 0
    while i < len(fruits1):
        print(fruits1[i])
        i = i + 1