"""
This example copied a list and assigned it to a new list using a slice. This keeps both lists the same unless changes to one another need to be made individually.

original_list = ['Breeding Pool', 'Stomping Ground', 'Watery Grave', 'Hallowed Fountain']
new_list = original_list[:]

original_list[1] = 'Sacred Foundry'
new_list[0] = 'Blood Crypt'

print(f'Original list: {original_list}\nCopied list:  {new_list}')
"""

"""
4-10: Slices
This exercise uses a list and slices it to display the first three items, the middle three items, and the last three items of the list on their own lines. 

shock_lands = ['Breeding Pool', 'Stomping Ground', 'Watery Grave', 'Sacred Foundry', 'Hallowed Fountain', 'Blood Crypt']

print(f'The first three items in the list of shock lands are:{shock_lands[:3]}')
# FIND A BETTER WAY TO FIND THE MIDDLE THREE ITEMS IN A LIST OF VARYING SIZE - COMPLETE THIS!!
print(f'The middle items in the list of shock lands are:{shock_lands[1:-2]}')
print(f'The last three items in the list of shock lands are:{shock_lands[-3:]}')
"""

"""
4-11 My pizzas, your pizzas
This exercise created a list and made a copy of it inside a new list. Then each list had an item added to it and the contents of each list printed. 

my_favorite_pizzas = ['cheese', 'veggie', 'hawaiian', 'peperoni']
friend_pizzas = my_favorite_pizzas[:]

# Add a new pizza to 'my_favorite_pizzas'
my_favorite_pizzas.append('jalapeno & mushroom')

# Add a new pizza to 'friend_pizzas'
friend_pizzas.append('meat lovers')

# FIGURE OUT AN ELEGANT WAY TO DISPLAY THE CONTENTS OF EACH LIST USING A FOR LOOP!!
print(f'My favorite pizzas are: {my_favorite_pizzas}')
print()
print(f'My friend Ronald\'s favorite pizzas are: {friend_pizzas}')
"""
