from tkinter import *
from random import *
answers = ["It's definitley possible.",
        "Ask me again in five minutes",
        "You\'ve got top be kidding",
        "Well of course, silly person.",
        "Are you serious?",
        "Not on your life",
        "Of course not, no",
        "No sane person would ask me that",
        "Could be.",]
def on_ask():
        n=randint(0,len(answers)-1)
        lbl.config(text=answers[n])

def on_exit():
    root.destroy()

root=Tk()
lbl=Label(root, text='Ask the Swami anything!',
                width=30, height=3)
lbl.pack()
exit_btn=Button(root,text='Exit', command=on_exit)
exit_btn.pack(side=LEFT,ipadx=25)
ask_btn=Button(root,text='Ask', command=on_ask)
ask_btn.pack(side=RIGHT, ipadx=25)
root.mainloop()       