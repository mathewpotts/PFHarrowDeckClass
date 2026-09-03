# PFHarrowDeckClass

A small Pathfinder 1e Harrow deck viewer and Python deck class. The project
includes the 54 Harrow cards, their alignments, and their associated ability
scores.

## Requirements

- Python 3
- Pillow
- Tkinter (included with most Python installations; on some Linux systems it
	is provided by a separate package)

Install Pillow with:

```text
python -m pip install Pillow
```

## Run the viewer

Run the script from the project directory so the relative `assets` path can be
resolved:

```text
python HarrowDeck.py
```

Click the deck image to draw a card. Use **Shuffle** to randomize the remaining
deck, or click the face-up card to return it to the deck. **File > Save** writes
the current deck state to `deck.pkl` in the current directory.

## Use the deck class

`HarrowDeck` can also be used without the GUI:

```python
from HarrowDeck import HarrowDeck

deck = HarrowDeck()
deck.shuffle()
card = deck.draw()
print(card)  # [card name, alignment, ability score]
```

The class also provides `remain()`, `drawn_cards()`, `add_cards_back()`, and
`save_deck()` for inspecting, returning, and saving cards.
