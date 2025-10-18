# This code creates a list and uses a range of numbers to work through then doubles each indexed value and appends the results to the created list.
"""squares = []
for num in range(1, 11, 2):
    squares.append(num ** 2)
print(squares)"""

"""ventura_ages = [54, 53, 34, 33, 30, 29, 27, 4]
print(f'Smallest age: {min(ventura_ages)}\nLargest age: {max(ventura_ages)}\nSum of ages: {sum(ventura_ages)}')
"""

"""
This code uses list comprehension on a list of names

names = ['SAMANTHA', 'CAMBRIA', 'CHRISTIAN', 'FUZZY']
list_redo = [name.title() for name in names]
print(list_redo)

This is the original for loop that gets replaced with the list comprehension
for name in names:
    x = name.title()
    print(x)
"""

"""for num in range(1, 21, 2):
    print(num)

count_20 = [num for num in range(1, 21)]
print(count_20)"""




"""
thislist = ['donut', 'chips', 'candy']
newlist = [food for food in range(len(thislist))]
print(thislist)
for junk in range(len(thislist)):
    print(thislist[junk])


million_list = []
for num in range(0, 10**10):
    print(num)
"""


"""million_list = []
for num in range(0, 10**6):
    million_list.append(num)
print(f'Max number: {max(million_list)}')
print(f'Min number: {min(million_list)}')"""

"""million_list = [a for a in range(0, 10**5) if a % 2 == 0]
print(million_list)"""

"""
This code cubes each number between 1 and 10 then adds them to the list_of_cubes list. 
list_of_cubes = []
for num in range(1, 11):
    num = num ** 3
    list_of_cubes.append(num)
print(list_of_cubes)"""

"""
This is the previous script except I used list comprehension to place the code in one line.
list_of_cubes = [num ** 3 for num in range(1, 11)]
print(list_of_cubes)"""

