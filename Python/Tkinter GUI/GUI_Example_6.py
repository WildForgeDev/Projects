from tkinter import *
window = Tk()
window.title('Welcome to Canvas')
Can = Canvas(window, bg = 'light blue', height = 280, 
width = 320)
coord = 20, 100, 240, 210
arc = Can.create_arc(coord, start = 0, extent = 150, fill = 'red')
line = Can.create_line(10,10,200,200,fill = 'white')
Can.pack()
mainloop()