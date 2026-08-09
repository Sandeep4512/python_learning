# list = [1, 2, 3, 4, 5]

# for item in list:
#     print(item * 2)

# for i in range(1, 10, 2):
#     print(i)


# count = 1  # initialize the count variable

# while count <= 5:  # condition to check if count is less than or equal to 5
    # print(count) # print the current value of count
    # count += 1  # update the count variable to avoid infinite loop


# range1 = range(1, 10)  # create a range object from 1 to 9
# for i in range1:  # iterate over the range object
    # print(i)  # print the current value of i


# print(list(range(1, 10)))  # print the range object

# fruits = ["Apple", "Banana", "Mango"]
# print(len(fruits))
# for i in range(3):
    # print(i)


# fruits = ["Apple", "Banana", "Mango"]
# print(list(enumerate(fruits)))

# for items in enumerate(fruits):
    # print(items)



# names = ["Sandeep", "Rahul", "Amit"]
# marks = [90, 85, 95]

# for name, mark in zip(names, marks):
    # print(name, mark)

students = [('A',90), ('B',80), ('C',70)]

names, marks = zip(*students)

print(names)
print(marks)

fruits = ["Apple", "Banana", "Mango"]
prices = [120, 60, 150]

# range()
# for i in range(len(fruits)):
    # print(i, fruits[i])

# enumerate()
# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# # zip()
# for fruit, price in zip(fruits, prices):
#     print(fruit, price)



# student = [1,2,3,4,5]

# while student:      
#     print(student.pop())  # remove and print the last student from the list



# name = "Python"
# for char in name:
#     print(char)
# number = 1
# sum = 0

# while number < 10:
#     sum = sum+ number
#     number= number+1
# print(f"sum : {sum}")

numbers = [10, 25, 30, 45, 50, 65]

# count=0
# sum=0
# for item in numbers:
#     if item >= 40:
#         sum=sum+item
#         count+=1
# print(f"count items:{count}")
# print(f"Sum of items:{sum}")

# numbers = [10, 25, 30, 45, 50, 65]

# how to get maximun number form the list 

# numbers = [10, 25, 30, 45, 50, 65,80,58,534]
# largest = numbers[0]
# for number in numbers:
#     if number < largest:
#         largest = number
# print("Largest number:", largest)

# ----------------------------------------------
# num = 10
# for i in range(1, num + 1):
#     for j in range(1, num + 1):
#         print(f"{i} * {j} = {i * j}", end="\t")
#     print()

# ------------------------------------------

# num= 5
# fact=1
# for item in range(1,num+1):
#     fact= fact*item
# print(f"Factorial of {num} is {fact}")

num = 34567
count =0
while num > 0:
    num = num/10
    count+=1
print(f"count digit {count}")
