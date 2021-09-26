from tkinter import *
import tkinter.messagebox as newwin
window = Tk()
window.title('Unit 5 Submission 1')
window.geometry('800x400')

def d1():
    mbox = newwin.askyesno('Look, a new window appears!', 'Continue?')
    if mbox == 1:
        newwin.showinfo('Yes','Great Choice!')
    else:
        newwin.showwarning('No','Goodbye')
    display.pack() 

btn_end = Button(window,text='Exit', command = window.quit)
btn_clickhere = Button(window,text='Click Here for a new window.', command=d1)
btn_end.pack(padx = 140 , pady = 30 )
btn_clickhere.pack(padx = 100, pady = 40)
mainloop()
