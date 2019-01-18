#Parker Daniels
#Estimates probability of rolling 5 of a kind on 6-sided dice while also displaying graphics for the dice.

import graphics as g
import tkinter
import random

def main():
    intro()
    dice=setup()



    tkinter.mainloop()
def intro():
    print("Rolls five dice simultaneously a given number of times and then outputs the number of times a 5 of a kind"
          " set was rolled and the percentage calculated.")

#plan to use dictionaries to store dice graphics. try 800 pix.
def setup():
    graph=g.GraphWin("Dice Probability",800,800)
    dice={}








main()