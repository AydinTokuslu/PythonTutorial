import random

class Card(object):
    def __init__(self, suit, value):
        self.suit= suit
        self.value = value
    def show_card(self):
        print("{} of {}".format(self.value, self.suit))
    pass
class Deck(object):  # kartlar
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
        #self.show_deck()
    def build(self):
        for s in ["Spades", "Diamonds", "Hearts", "Clubs"]:  # Maça, Karo, Kupa, Sinek
            for v in range(1,14):
                self.cards.append(Card(s,v))
    def show_deck(self):
        for card in self.cards:
            card.show_card()
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def draw_card(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand =[]
    def draw(self,deck):
        self.hand.append(deck.draw_card())
        return self
    def show_hand(self):
        for card in self.hand:
            card.show_card()
    def discard(self):
        return self.hand.pop()

def main():
    deck = Deck()
    deck.shuffle()
    Ali = Player("Ali")
    Ahmet = Player("Ahmet")
    Mehmet = Player("Mehmet")
    Veli = Player("Veli")
    Ali.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
    Ahmet.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
    Mehmet.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
    Veli.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
    print("Ali's hand : ")
    Ali.show_hand()
    print("--------------")
    print("Ahmet's hand : ")
    Ahmet.show_hand()
    print("--------------")
    print("Mehmet's hand : ")
    Mehmet.show_hand()
    print("--------------")
    print("Veli's hand : ")
    Veli.show_hand()



main()