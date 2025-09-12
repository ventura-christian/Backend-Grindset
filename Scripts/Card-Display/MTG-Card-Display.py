"""
This script will store a list of card names. When the user enters a card name, it will determine if the card is in the list.
- Create a function to store list of card names.
- Add logic to determine if the requested card is in the list. 
- Create main function
- Add a prompt message for the user along with functionality to exit or continue the program based on user input. 
- Run program and test. 
"""

# Feel free to add or subtract cards from this list and test to see what happens if the card you choose is not in the included list. This is for testing and running purposes to showcase that I can make a simple python script that does something. 

# If your not familiar with Magic: the Gathering, refer to https://scryfall.com and use the 'Random Card' button to give you cards to add to list. 

def card_database(cardname):
    card_list = [
        "Bloodstained Mire", "Flooded Strand", "Polluted Delta", "Windswept Heath", "Wooded Foothills", "Arid Mesa", "Misty Rainforest", "Scalding Tarn", "Verdant Catacombs", "Marsh Flats", "Black Lotus", "Ancestral Recall", "Time Walk", "Timetwister", "Mox Pearl", "Mox Sapphire", "Mox Jet", "Mox Ruby", "Mox Emerald"
    ]
    
    if cardname in card_list:
        return f"{cardname} is in the list!\n"
    else:
        return f"{cardname} is not in the list.\n"
    
def main():
    print()
    card_choice = input('Please enter a Magic: the Gathering card name\n---------------------------------------------\n>>')
    if card_choice != 'exit':
        print(card_database(card_choice))
        return main()
    else:
        print('\nThank you for using this program!')
    
main()
