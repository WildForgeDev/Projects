from tkinter import *
window = Tk()
window.title('Rectangle Example')
Can = Canvas(window, width=220, height=110)
Can.pack()
Can.create_rectangle(50, 20, 150, 80, fill="dark gray")
Can.create_rectangle(65, 35, 135, 65, fill="light blue")
mainloop()
