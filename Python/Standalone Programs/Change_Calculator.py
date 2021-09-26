from tkinter import * # Import TK Interface Library

mainbox = Tk() # Create the main gui box to house Labels, Buttons, Entry Boxes, Etc. 
mainbox.title('Change Calculator')

#Labels for each entry box/total
Label(mainbox, text="Pennies:").grid(row=1) #Creates labels for all entry/total boxes.
Label(mainbox, text="Nickels:").grid(row=2)
Label(mainbox, text="Dimes:").grid(row=3)
Label(mainbox, text="Quarters:").grid(row=4)
Label(mainbox, text="Half-Dollars:").grid(row=5)
Label(mainbox, text="Dollar Coins:").grid(row=6)
Label(mainbox, text="Total:").grid(row=1, column=3)
Label(mainbox, text="Total:").grid(row=2, column=3)
Label(mainbox, text="Total:").grid(row=3, column=3)
Label(mainbox, text="Total:").grid(row=4, column=3)
Label(mainbox, text="Total:").grid(row=5, column=3)
Label(mainbox, text="Total:").grid(row=6, column=3)

#Labels for the grand totals
Label(mainbox, text="Total Change: $").grid(row=7, column=3) #Create a grand total label

# Label(mainbox, text="Placeholder").grid(row=7, column=4)

# Total
totalChangeValueText = StringVar() #Create string variables to add total amounts as strings to GUI.
totalChangeValueText.set('')
Label(mainbox, textvariable = totalChangeValueText).grid(row=7, column=4) 

# Penny String Variable
pennyValueText = StringVar()
pennyValueText.set('')
Label(mainbox, textvariable=pennyValueText).grid(row=1, column=4)

# Nickel String Variable
nickelValueText = StringVar()
nickelValueText.set('')
Label(mainbox, textvariable=nickelValueText).grid(row=2, column=4)

# Dime String Variable
dimeValueText = StringVar()
dimeValueText.set('')
Label(mainbox, textvariable=dimeValueText).grid(row=3, column=4)

# Quarter String Variable
quarterValueText = StringVar()
quarterValueText.set('')
Label(mainbox, textvariable=quarterValueText).grid(row=4, column=4)

# Half-Dollar String Variable
halfdollarValueText = StringVar()
halfdollarValueText.set('')
Label(mainbox, textvariable=halfdollarValueText).grid(row=5, column=4)

# Dollar Coin String Variable
dollarcoinValueText = StringVar()
dollarcoinValueText.set('')
Label(mainbox, textvariable=dollarcoinValueText).grid(row=6, column=4)

#Entry Boxes
e1 = Entry(mainbox) # Create Entry boxes to allow for user entry of coin amounts.
e2 = Entry(mainbox) # Assign variable names to entry boxes for function manipulation.
e3 = Entry(mainbox)
e4 = Entry(mainbox)
e5 = Entry(mainbox)
e6 = Entry(mainbox)

#Entry Box Placement 
e1.grid(row=1, column=1) #Place entry boxes in specific orientation on the grid of the GUI.
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)

#Calculate Button Function 
def convert(): # Define Function
        try:
            c1 = float(e1.get())*.01 # Math performed on entry to get value and assign it to a string variable
            if c1 <= 0: # Check for entries less than 0 to account for negatrive entries
                c1 = 0 # Assigns the value to 0 if negative number is entered.
                pennyValueText.set(c1) # Assigns value to string varable for display in the GUI.
            elif c1 <= .00999999: # Check for entries between 0 and 1 to account for fractional entries.
                c1 = 0 # Assigns the value to 0 if fraction/decimal number is entered.
                pennyValueText.set(c1) # Assigns value to string varable for display in the GUI.
            else:
                pennyValueText.set(c1) # Assigns value to string varable for display in the GUI.
        except ValueError: # Exception for string entries to ensure this error is handled
            c1 = "Error" # Assigns "Error" value to variable in order to display in GUI
            pennyValueText.set(c1) #Assigns the error value to the string variable to display in GUI
        
        try: # Repeated code for other coin amounts (see above for explanation)
            c2 = float(e2.get())*.05
            if c2 < 0:
                c2 = 0
                nickelValueText.set(c2)
            elif c2 <= .04999995:
                c2 = 0
                nickelValueText.set(c2)
            else:
                nickelValueText.set(c2)
        except ValueError:
            c2 = "Error"
            nickelValueText.set(c2)
        
        try: # Repeated code for other coin amounts (see above for explanation)
            c3 = float(e3.get())*.1
            if c3 < 0:
                c3 = 0
                dimeValueText.set(c3)
            elif c3 <= .099999999:
                c3 = 0
                dimeValueText.set(c3)
            else:
                dimeValueText.set(c3)
        except ValueError:
            c3 = "Error"
            dimeValueText.set(c3)

        try: # Repeated code for other coin amounts (see above for explanation)
            c4 = float(e4.get())*.25
            if c4 < 0:
                c4 = 0
                quarterValueText.set(c4)
            elif c4 <= .249999975:
                c4 = 0
                quarterValueText.set(c4)
            else:
                quarterValueText.set(c4)
        except ValueError:
            c4 = "Error"
            quarterValueText.set(c4)

        try: # Repeated code for other coin amounts (see above for explanation)
            c5 = float(e5.get())*.5
            if c5 < 0:
                c5 = 0
                halfdollarValueText.set(c5)
            elif c5 <= .49999995:
                c5 = 0
                halfdollarValueText.set(c5)
            else:
                halfdollarValueText.set(c5)
        except ValueError:
            c5 = "Error"
            halfdollarValueText.set(c5)
        
        try: # Repeated code for other coin amounts (see above for explanation)
            c6 = float(e6.get())*1
            if c6 < 0:
                c6 = 0
                dollarcoinValueText.set(c6)
            elif c6 <= .9999999999999:
                c6 = 0
                dollarcoinValueText.set(c6)
            else:
                dollarcoinValueText.set(c6)
        except ValueError:
            c6 = "Error"
            dollarcoinValueText.set(c6)
        
        test = "" # declare the test variable for assignment
        if c1 == "Error":  # Handling for if a variable returns an error to avoid the total repeating "error" for each instance.
            test == "Error" # Assigns the value to test if error occurs.
            totalChangeValueText.set(test) # Assigns the error message to display if error occurs
        elif c2 == "Error": #Repeated Code (see above for explanation)
            test == "Error"
            totalChangeValueText.set(test)
        elif c3 == "Error": #Repeated Code (see above for explanation)
            test == "Error"
            totalChangeValueText.set(test)
        elif c4 == "Error": #Repeated Code (see above for explanation)
            test == "Error"
            totalChangeValueText.set(test)
        elif c5 == "Error": #Repeated Code (see above for explanation)
            test == "Error"
            totalChangeValueText.set(test)
        elif c6 == "Error": #Repeated Code (see above for explanation)
            test == "Error"
            totalChangeValueText.set(test)
        else: # If all the values are valid the sum of each value is assigned to the test variable
            test = c1+c2+c3+c4+c5+c6                     
            totalChangeValueText.set(test) # Assigns test value to string variable to be displayed in the GUI.

#Buttons
b1 = Button(mainbox, text = "Calculate", command=convert) #Create the calculate button to run the function to calculate coin amounts
b1.grid(row=7, column=0) # Assigns button to specific location in GUI. 
b2 = Button(mainbox, text = "Quit", command=mainbox.quit) #Create the quit button to quit the program.
b2.grid(row=7, column=1) # Assigns button to specific location in GUI. 

mainbox.mainloop() #Loops program so it does not close after running once.
