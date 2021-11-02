"""
File: dicedemo.py
Author: Le Trong
Date: 28/10/21
Pops up a window that allows the user to roll

"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from die import Die

class DiceDemo(EasyFrame):
    def __init__(self):
        """Creates the dice, and sets up the Images and
        labels for the two dice to be displayed,
        the state label, and the two command buttons."""
        EasyFrame.__init__(self, title="Dice Demo")
        self.setSize(220, 200)
        self.die1 = Die()
        self.die2 = Die()
        self.dieLabel1 = self.addLabel("", row=0, column=0, sticky="NSEW")
        self.dieLabel2 = self.addLabel("", row=0, column=1, sticky="NSEW", columnspan=2)
        self.stateLabel = self.addLabel("", row=1, column=0, sticky="NSEW", columnspan=2)
        self.addButton(row=2, column=0, text="Roll",  command=self.nextRoll)
        self.addButton(text="New game", row=2, column=1, command=self.newGame)
        self.refreshImages()

    def nextRoll(self):
        """Rolls the dice and updates the view with
            the results."""
        self.die1.roll()
        self.die2.roll()
        total = self.die1.getValue() + self.die2.getValue()
        self.stateLabel["text"] = "Total = " + str(total)
        self.refreshImages()

    def newGame(self):
        """Create new dice and updates the view."""
        self.die1 = Die()
        self.die2 = Die()
        self.stateLabel["text"] = ""
        self.refreshImages()

    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "DICE/dice-" + str(self.die1) + "-1.gif.png"
        fileName2 = "DICE/dice-" + str(self.die2) + "-1.gif.png"
        self.image1 = PhotoImage(file=fileName1)
        self.dieLabel1["image"] = self.image1
        self.image2 = PhotoImage(file=fileName2)
        self.dieLabel2["image"] = self.image2


def play_game_loop():
    """
    Instantiate and pop up the window.
    :return:
    """
    DiceDemo().mainloop()

if __name__ == '__main__':
    play_game_loop()