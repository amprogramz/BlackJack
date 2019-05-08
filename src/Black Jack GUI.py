from tkinter import *
from tkinter import ttk
import card_class

def hit_command():
    print('command line ran')


def fold_command(thing):
    print('command 2 ran', thing)


def sample_deck():
    deck = card_class.Deck()
    print(deck)
    show_cards(deck.deck_list[0], deck.deck_list[1])


def show_cards(*cards):
    i = 0
    a.card_list = []
    for card in cards:
        a.card_list.append(PhotoImage(
            file='.\\src\\Playing Cards\\Playing Cards\\PNG-cards-1.3\\' + card.face_value.lower() + '_of_clubs.png')\
            .subsample(5))
        #a.canvas = Canvas(a.window, width=600, height=300)
        #a.canvas.pack(expand=YES, fill=BOTH)
        a.canvas.create_image(i*30+100, i*30+10, anchor=NW, image=a.card_list[i])
        i += 1
        print('show cards run', i)
    print(a.card_list)


class UIFrame:
    button_list = {'Hit': lambda: hit_command(),
                   'Fold': lambda: fold_command('thing'),
                   'Show Cards': lambda: show_cards('place holder'),
                   'Get a deck': lambda: sample_deck()}

    def __init__(self, window):
        self.window = window
        i = 1
        c = 0
        for button in self.button_list:  # command to be set
            self.added_button = Button(window, text=button, command=self.button_list.get(button))
            self.added_button.grid(column=c, row=i)
            if i%2 == 0:
                c += 1
            i += 1
        self.canvas = Canvas(window, width=300, height=200)
        #self.canvas.pack(expand=YES, fill=BOTH).grid()
        self.canvas.grid(column=0, row=0)



root = Tk()
a = UIFrame(root)
root.mainloop()


