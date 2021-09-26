from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title( 'Choose the game you want to play.' )
frame = Frame( window )
game = StringVar()
radio_1 = Radiobutton( frame , text = 'RPG' , variable = game , value = 'You chose an RPG game.' )
radio_2 = Radiobutton( frame , text = 'Fighting' , variable = game , value = 'You chose a fighting game' )
radio_3 = Radiobutton( frame , text = 'Racing' , variable = game , value = 'You chose a Racing game' )
radio_4 = Radiobutton( frame , text = 'Puzzle' , variable = game , value = 'You chose a Puzzle game' )
radio_1.select()
def dialog() :   
    box.showinfo( 'You Selected' , 'Game Choice: \n' + game.get())
btn = Button( frame , text = 'Choose a game' , command = dialog )
btn.pack( side = RIGHT , padx = 5 )
radio_1.pack( side = LEFT )
radio_2.pack( side = LEFT )
radio_3.pack( side = LEFT )
radio_4.pack( side = LEFT )
frame.pack( padx = 30 , pady = 30 )
mainloop()