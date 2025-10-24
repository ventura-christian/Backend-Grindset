"""
For loops practice
"""

"""I'm not using a docstring correctly and that's why its not working as
it should
"""

magic_cards = ['dark confidant', 'polluted delta', 'thoughtseize', 
'jace, the mind sculptor']

for card in magic_cards:
    if card == 'dark confidant':
        print((f'{magic_cards[0].title()} is a creature card and \
costs 1 black and 1 generic mana.'))
    elif card == 'polluted delta':
        print(f'{magic_cards[1].title()} is a land, \
it doesn\'t cost any mana to cast.')
    elif card == 'thoughtseize':
        print(f'{magic_cards[2].title()} is a sorcery spell and \
costs 1 black mana to cast')
    elif card == 'jace, the mind sculptor':
        print(f'{magic_cards[-1].title()} is a planeswalker and \
costs 2 blue and 2 generic mana to cast.')
        
print('These are only a small example of the vast types of cards \
that exist in the trading card game Magic: the Gathering.') 
