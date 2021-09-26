from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title( 'Entry Widget' )
frame = Frame( window )
entry = Entry( frame )
def dialog():  
    box.showinfo( 'Display Text' , 'You entered, ' + entry.get())
b1=Button(frame , text = 'Enter Your text here.', command = dialog )
b1.pack( side = RIGHT , padx = 6 )
entry.pack( side = LEFT )
frame.pack( padx = 50 , pady = 50 )
mainloop()