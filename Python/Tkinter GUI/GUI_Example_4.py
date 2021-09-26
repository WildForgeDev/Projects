from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title( 'Unit 5 Listbox' )
frame = Frame( window )
label = Label(window, text = 'What are you going to eat today?')
label.pack(padx = 5, pady = 5)
listbox = Listbox( frame )
listbox.insert( 1, 'Tacos' )
listbox.insert( 2, 'Spaghetti' )
listbox.insert( 3, 'Cheeseburger' )
listbox.insert( 4, 'Salad' )
def dialog() :   
    box.showinfo( 'Selection Made' , 'Your Choice: ' + \
    listbox.get( listbox.curselection() ) )
btn = Button( frame, text = 'Choose', command=dialog )
btn.pack( side = RIGHT , padx = 6 )
listbox.pack( side = LEFT )
frame.pack( padx = 60, pady = 60 )
mainloop()

