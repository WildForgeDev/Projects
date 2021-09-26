from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title( 'Using a Message Box' )
def dialog() :
    var = box.askyesno( 'Showing a Message' , 'Continue?' )   
    if var == 1 :     
        box.showinfo( 'Yes', 'Continuing...' )   
    else :      
        box.showwarning( 'No', 'Ending...' )
btn = Button( window , text = 'Click Me' , command=dialog )
btn.pack( padx = 180 , pady = 80 )
mainloop()
