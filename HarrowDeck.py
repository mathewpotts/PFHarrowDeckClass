
from itertools import product
from random import shuffle

class HarrowDeck():
    def __init__(self, type='pfharrow'):
        if type == 'pfharrow':
            # Taken from https://www.d20pfsrd.com/magic-items/artifacts/minor-artifacts/deck-of-many-things-harrow
            cards = [
            ['The Avalanche','LE'], ['The Bear','N'],['The Beating','NE'], ['The Betrayal','NE'],['The Big Sky','CG'], ['The Brass Dwarf','LN'],
            ['The Carnival','CN'], ['The Courtesan','CN'],['The Cricket','NG'], ['The Crows','NE'],['The Cyclone','CE'], ['The Dance','LG'],
            ["The Demon's Lantern",'CE'], ['The Desert','CG'],['The Fiend','LE'], ['The Foreign Trader','N'],['The Forge','LN'], ['The Eclipse','LE'],
            ['The Empty Throne','LG'], ['The Hidden Truth','LG'],['The Idiot','NE'], ['The Inquisitor','LN'],['The Joke','CG'], ['The Juggler','CG'],
            ['The Keep','NG'], ['The Liar','CE'],['The Locksmith','LN'], ['The Lost','CE'],['The Marriage','LN'], ['The Midwife','NG'],
            ['The Mountain Man','CN'], ['The Mute Hag','NE'],['The Owl','N'], ['The Paladin','LG'],['The Peacock','N'], ['The Publican','CG'],
            ['The Queen Mother','LN'], ['The Rabbit Prince','CN'],['The Rakshasa','LE'], ['The Sickness','NE'],['The Snakebite','CE'], ['The Survivor','NG'],
            ['The Tangled Briar','LE'], ['The Teamster','N'],['The Theater','NG'], ['The Trumpet','LG'],['The Twin','N'], ['The Tyrant','LE'],
            ['The Unicorn','CG'], ['The Uprising','CN'],['The Vision','CN'], ['The Wanderer','NG'],['The Waxworks','CE'], ['The Winged Serpent','LG'],
            ]
            # abliity catagories https://pathfinder.fandom.com/wiki/List_of_harrow_cards
            abilities_dict = {
                'str' : ['The Paladin','The Keep','The Big Sky','The Forge','The Bear','The Uprising','The Fiend','The Beating','The Cyclone'],
                'dex' : ['The Dance','The Cricket','The Juggler','The Locksmith','The Peacock','The Rabbit Prince','The Avalanche','The Crows',"The Demon's Lantern"],
                'con' : ['The Trumpet','The Survivor','The Desert','The Brass Dwarf','The Teamster','The Mountain Man','The Tangled Briar','The Sickness','The Waxworks'],
                'int' : ['The Hidden Truth','The Wanderer','The Joke','The Inquisitor','The Foreign Trader','The Vision','The Rakshasa','The Fool','The Snakebite'],
                'wis' : ['The Winged Serpent','The Midwife','The Publican','The Queen Mother','The Owl','The Carnival','The Eclipse','The Mute Hag','The Lost'],
                'cha' : ['The Empty Throne','The Theater','The Unicorn','The Marriage','The Twin','The Courtesan','The Tyrant','The Betrayal','The Liar']
            }
            # Combine cards and abilities
            for a, c in abilities_dict.items():
                for card in cards:
                    if card[0] in c:
                        card.append(a.upper())
            self.deck = cards
    @staticmethod
    def shuffle(self):
        return shuffle(self.deck)
    @staticmethod
    def draw(self):
        if self.deck:
            card = self.deck.pop(0)
            return f'Card: {card[0]}, Alignment: {card[1]}, Ability: {card[2]}'
        else:
            return "Deck is empty!"
    @staticmethod
    def remain(self):
        return len(self.deck)
