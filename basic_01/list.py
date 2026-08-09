# list and method

# my_list = [1, 2, 3, 4, 5]
# my_list.append(7)
# print(f"List after append: {my_list}")
# print("list after append: ", my_list)

# print(f"first index of list: {my_list[0]}")
# print(f"last index of list: {my_list[-1]}")
# print(f"length of list: {len(my_list)}")

fruits1 = {"apple", "banana", "cherry", "kiwi", "mango"}
fruits2 = {"banana", "kiwi", "grapes", "orange", "papaya"}

combine_fruits = fruits1 | fruits2
print(f"union fruits: {combine_fruits}")

common_fruits = fruits1 & fruits2
print(f"common fruits: {common_fruits}")

remove_fruits = fruits1 - fruits2
print(f"remove fruits: {remove_fruits}")

# number = {1, 2, 3, 4, 5} first way to create set
# number = set([1, 2, 3, 4, 5]) # second way to create set
# number = set(range(1, 6)) # third way to create set
# number = set() # fourth way to create set
number = {1, 2, 3, 4, 5}
print(f"number: {type(number)}")

number2 = set()
number2.add(6)
number2.add(7)
number2.add(8)  
print(f"number2: {number2}")

# duplicate values are not allowed in set
number3 = {1, 2, 3, 4, 5, 5, 5}  # This will only contain unique values
print(f"number3: {len(number3)}")

print(f"check 5 in number3: {100 not in number3}")

number3.add(50)
print(f"number3 after add: {number3}")
# number3.update(80, 90, 100)
number3.update({80, 90, 100})  # Correct way to update with multiple values
print(f"number3 after update: {number3}")

# number3.remove(1000) # This will raise a KeyError if 1000 is not in the set
# print(f"number3 after remove: {number3}")

number3.discard(90)  # discard does not raise an error if the element is not found
print(f"number3 after discard: {number3}")

number3.clear()  # This will remove all elements from the set
print(f"number3 after clear: {number3}")

# del number3  # This will delete the set entirely
# print(f"number3 after delete: {number3}")  # This will raise a NameError since number3 is deleted

# number2.copy()  # This will create a shallow copy of number2
print(f"number2: {number2}")
print(f"number2 copy: {number2.copy()}")

A = {1, 2, 3}
B = {3, 4, 5}

print(f"Symmetric difference: {A ^ B}")  # Elements in either A or B but not in both

print(A | B)  # Union of A and B
print(A & B)  # Intersection of A and B 


