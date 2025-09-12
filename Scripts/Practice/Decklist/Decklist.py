"""
This program will take several lists of cardnames and print them neatly as a reference decklist for Magic: the Gathering players.
1. Store card types sorcery, instant, land, and creature in individual lists. 
2. Populate each list with cardnames. 
3. Print the cards within each list based on type and display the number of copies present within the list. 
What next?
    - Create functions to store the lists based on card types.
    - Add funcitonality to loop through the lists to count the number of each individual card for easier printing.
    - Add functionality to add or remove cards from each list. 
    - Implement functionality to display the quantity of requested card names or types based on values stored in variables. For example, if “brainstorm” is requested, the program should return the number of copies recorded in a list held within a variable.
"""

sorcery = ['Treasure Cruise']
instant = ['Brainstorm', 'Brainstorm', 'Brainstorm', 'Brainstorm', 'Fatal Push', 'Fatal Push', 'Fatal Push', 'Swords to Plowshares', 'Swords to Plowshares', 'Swords to Plowshares', 'Swords to Plowshares', 'Mana Drain', 'Mana Drain', 'Mana Drain', 'Flare of Denial', 'Flare of Denial', 'Flare of Denial', 'Flare of Denial']
land = ['Island', 'Hallowed Fountain', 'Hallowed Fountain', 'Breeding Pool', 'Strip Mine', 'Strip Mine', 'Strip Mine', 'Flooded Strand', 'Flooded Strand', 'Flooded Strand', 'Flooded Strand']
creature = ['Deathrite Shaman', 'Deathrite Shaman', 'Deathrite Shaman', 'Deathrite Shaman', 'Phantasmal Shieldback', 'Phantasmal Shieldback', 'Phantasmal Shieldback', 'Phantasmal Shieldback', 'Tamiyo, Inquisitive Student', 'Tamiyo, Inquisitive Student', 'Tamiyo, Inquisitive Student', 'Tamiyo, Inquisitive Student', 'Psychic Frog', 'Psychic Frog', 'Psychic Frog', 'Psychic Frog', 'Luurus of the Dream Den']

print('\n')
print('Decklist:\'Tamiyo Frog\'\nFormat: Timeless\n')
print(f'Sorceries\n----------------\n 1 {sorcery[0]}\n')
print(f'Instants\n----------------\n 4 {instant[0]}\n 3 {instant[4]}\n 4 {instant[7]}\n 3 {instant[11]}\n 4 {instant[14]}\n')
print(f'Lands\n----------------\n 1 {land[0]}\n 2 {land[1]}\n 1 {land[3]}\n 3 {land[4]}\n 4 {land[7]}\n')
print(f'Creatures\n----------------\n 4 {creature[0]}\n 4 {creature[4]}\n 4 {creature[8]}\n 4 {creature[12]}\n 1 {creature[16]}\n')




        
