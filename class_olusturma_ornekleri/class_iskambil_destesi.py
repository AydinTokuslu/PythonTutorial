class Card(object):
    def __init__(self, suit, value):
        self.suit= suit
        self.value = value
    def show_card(self):
        print("{} of {}".format(self.value, self.suit))
    pass
class Deck(object):  # kartlar
    pass
class Player(object):
    pass

def main():
    card = Card("Hearts", 10)  # Hearts = Kupa

main()