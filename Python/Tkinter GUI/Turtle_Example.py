import turtle #We are importing turtle
class Click1: #Naming the class Click1
    def __init__(self):
        self.t = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.setup(260,260) #Defining the box to be 260 by 260
        self.wn.onclick(self.t.goto)

    def main(self):
        turtle.mainloop() #The main loop for turtle

Click1().main()
