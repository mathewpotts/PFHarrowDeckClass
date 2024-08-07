#!/usr/bin/env python3
################################################################################
### Import Libraries ###########################################################
################################################################################
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import shuffle
from glob import glob
import pickle


################################################################################
#### Classes ###################################################################
################################################################################
class HarrowDeck:
    def __init__(self, type='pfharrow'):
        if type == 'pfharrow':
            # Taken from https://www.d20pfsrd.com/magic-items/artifacts/minor-artifacts/deck-of-many-things-harrow
            cards = [
            ['The Avalanche','LE'], ['The Bear','N'],['The Beating','NE'], ['The Betrayal','NE'],['The Big Sky','CG'], ['The Brass Dwarf','LN'],
            ['The Carnival','CN'], ['The Courtesan','CN'],['The Cricket','NG'], ['The Crows','NE'],['The Cyclone','CE'], ['The Dance','LG'],
            ["The Demon's Lantern",'CE'], ['The Desert','CG'],['The Fiend','LE'], ['The Foreign Trader','N'],['The Forge','LN'], ['The Eclipse','LE'],
            ['The Empty Throne','LG'], ['The Hidden Truth','LG'], ['The Idiot','NE'], ['The Inquisitor','LN'],['The Joke','CG'], ['The Juggler','CG'],
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
                'int' : ['The Hidden Truth','The Wanderer','The Joke','The Inquisitor','The Foreign Trader','The Vision','The Rakshasa','The Idiot','The Snakebite'],
                'wis' : ['The Winged Serpent','The Midwife','The Publican','The Queen Mother','The Owl','The Carnival','The Eclipse','The Mute Hag','The Lost'],
                'cha' : ['The Empty Throne','The Theater','The Unicorn','The Marriage','The Twin','The Courtesan','The Tyrant','The Betrayal','The Liar']
            }
            # Combine cards and abilities
            for a, c in abilities_dict.items():
                for card in cards:
                    if card[0] in c:
                        card.append(a.upper())
            self.deck = cards
            self.drawn_cards_list = []

    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        if self.deck:
            card = self.deck.pop(0)
            self.drawn_cards_list.append(card)
            return card
        else:
            return None

    def remain(self):
        return len(self.deck)

    def drawn_cards(self):
        drawn_cards = []
        for card in self.drawn_cards_list:
            drawn_cards.append(card)
        return drawn_cards

    def add_cards_back(self, card_names):
        if isinstance(card_names, str):
            card_names = [card_names]
        for card_name in card_names:
            card = next((card for card in self.drawn_cards_list if card[0] == card_name), None)
            if card:
                self.deck.append(card)
                self.drawn_cards_list.remove(card)
                print(f'Card {card_name} added back to the deck.')
            else:
                print(f'Card {card_name} is not in the drawn cards list.')

    def save_deck(self):
        deck = {}
        deck['Deck'] = self.deck
        deck['DrawnCards'] = self.drawn_cards_list
        with open('deck.pkl','wb') as f:
            pickle.dump(deck,f)

class HarrowGUI:
    def __init__(self, root):
        self.root = root

        # Window title
        self.root.title("Harrow Deck Viewer")

        # Init Deck Class
        self.deck = HarrowDeck()

        # Create a menubar
        menubar = tk.Menu()
        root.config(menu=menubar)

        #Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_file)

        # Set up Card remaining label
        self.card_remaining = tk.StringVar()
        self.card_remaining.set(f"Number of Cards in Deck: {self.deck.remain()}")
        remainLabel = tk.Label(root, textvariable = self.card_remaining)
        remainLabel.grid(row = 0, column = 0, columnspan=2)

        # Set up Card Properties Label
        self.card_props = tk.StringVar()
        card_props_ali_label = tk.Label(root, textvariable = self.card_props)
        card_props_ali_label.grid(row = 1, column = 3)

        # Deck images
        DeckBack_path = 'assets\stackfulldeck.png'
        self.card_images = glob(f'assets\*')
        self.im = Image.open(DeckBack_path)
        self.imWidth, self.imHeight = self.im.size
        self.DeckBack = ImageTk.PhotoImage(self.im) # get the image import into tkinter
        width,height = Image.open(DeckBack_path).size
        self.DeckBack_im = tk.Button(root, image = self.DeckBack, command = self.draw_card)
        self.DeckBack_im.grid(column=0, row=1)
        self.root.grid_columnconfigure(1,minsize=self.imWidth)

        # Init face up card image as None
        self.DeckFace_im = None

        # Widgets Buttons
        shuffle_button = tk.Button(root, text = 'Shuffle', command = self.shuffle)
        # more to come...
        buttons = [shuffle_button,]
        for i,button in enumerate(buttons):
            button.grid(column=0+i, row=2)

    def draw_card(self):
        card = self.deck.draw()
        if card is None:
            print("Deck is empty!")
        else:
            print(card[0])
            card_im = [im for im in self.card_images for c in card[0].lower().split()[1:] if c in im]
            print(card_im)
            self.DeckFace = ImageTk.PhotoImage(Image.open(card_im[0])) # get the image import into tkinter
            if self.DeckFace_im:
                self.DeckFace_im.config(image=self.DeckFace)
                self.DeckFace_im.image = self.DeckFace
            else:
                self.DeckFace_im = tk.Button(self.root, image = self.DeckFace, command = self.return_card)
                self.DeckFace_im.image = self.DeckFace
                self.DeckFace_im.grid(column=1, row=1)
            self.update_remains()
            self.update_card_props()

    def update_remains(self):
        self.card_remaining.set(f"Number of Cards in Deck: {self.deck.remain()}")

    def update_card_props(self):
        if self.deck.remain() < 54:
            name, alignment, attribute = self.deck.drawn_cards()[-1]
            self.card_props.set(f'Alignment: {alignment}\nAbility: {attribute}')
        else:
            self.card_props.set('')

    def shuffle(self):
        self.deck.shuffle()
        print('deck is shuffled')

    def return_card(self):
        self.deck.add_cards_back(self.deck.drawn_cards()[-1][0])
        if self.deck.remain() < 54:
            card = self.deck.drawn_cards()[-1][0]
            card_im = [im for im in self.card_images for c in card.lower().split()[1:] if c in im]
            self.DeckFace = ImageTk.PhotoImage(Image.open(card_im[0])) # get the image import into tkinter
            self.DeckFace_im.config(image=self.DeckFace)
            self.DeckFace_im.image = self.DeckFace
        else:
            self.DeckFace_im.destroy()
            self.DeckFace_im = None
        self.update_remains()
        self.update_card_props()

    def save_file(self):
        messagebox.showinfo("Save", "Save option selected")
        self.deck.save_deck()

    def load_file(self):
        messagebox.showinfo("Load", "Load option selected")

################################################################################
#### Functions #################################################################
################################################################################
# Function to handle the Save option
def GUI():
    root = tk.Tk()
    root.geometry() # set default window size
    app = HarrowGUI(root)
    root.mainloop()

if __name__ == "__main__":
    GUI()
