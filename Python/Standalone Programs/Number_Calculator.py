while True:
    print("Intellipath Unit 2, section 2 submission program")
    
    var1 = int(input("Please enter the first variable: ")) # User inputs variable 1
    var2 = int(input("Please enter the second variable: "))# User inputs variable 2
    var3 = int(input("Please enter the third variable: "))# User inputs variable 3

    Calc1 = var1 + var2 + var3 # Calculates the sum of the user input variables
    Calc2 = Calc1 / 3 # Calculates the average of the user input variables
    Calc3 = var1 * var2 * var3 # Calculates the products of the user input variables
    Calc4 = min(var1, var2, var3) # Calculates the minimum of the user input variables
    Calc5 = max(var1, var2, var3) # Calculates the maximum of the user input variables

    print("The sum of",var1,",",var2,",","and",var3, "is:", Calc1) # prints the Sum of the user input variables
    print("The average of",var1,",",var2,",","and",var3, "is:", Calc2) # prints the average of the user input variables
    print("The product of",var1,",",var2,",","and",var3, "is:", Calc3) # prints the product of the user input variables
    print("The smallest number of",var1,",",var2,",","and",var3, "is:", Calc4) # prints the minimum of the user input variables
    print("The largest number of",var1,",",var2,",","and",var3, "is:", Calc5) # prints the maximum of the user input variables

    answer = input("Would you like to calculate three more numbers? key yes/no: ") # Statement asking user if they would like to calculate three more numbers.
    if answer not in ("yes", "no"): # Statement that handles non yes/no inputs.
        print("Input not valid")
        break
    if answer == "yes": # Reiterates the program when user answers yes to converting another three more numbers.
        continue
    else:
        input("\nPress the enter key to exit") # Exits the program when user does not want to calculate any more numbers.
        break
    

