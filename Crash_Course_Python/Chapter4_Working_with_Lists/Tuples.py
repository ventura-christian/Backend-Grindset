"""
This script introduces tuples and f strings to produce text based on the contents of the tuple.

ventura_family = ('fuzzy', 'samantha', 'cambria', 'christian')
for member in ventura_family:
    if member == 'fuzzy':
        print(f'This is {member}, she\'s a cat.')
    if member == 'samantha':
        print(f'This is {member}, she\'s {ventura_family[2]}\'s mom and {ventura_family[3]}\'s husband.')
    if member == 'cambria':
        print(f'This is {member}, she\'s {ventura_family[1]} and {ventura_family[3]}\'s daughter.')
    if member == 'christian':
        print(f'This is {member}, he\'s {ventura_family[1]}\'s husband and {ventura_family[2]}\'s dad.')  
"""

# 4-13: Buffet
basic_foods = ('burger', 'grilled cheese', 'quesadilla', 'soup', 'pizza')
basic_foods[1] = 'mac \'n cheese';
print(basic_foods)


# for food in basic_foods:
#     print(food.title())
# print(basic_foods)