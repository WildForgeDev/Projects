while True:
    int1 = int(input("Enter the integer to determine if it is odd or even: ")) #User input for the integer being tested for odd/even.
    mod1 = int1 % 2 #uses the modulus of 2 to break the user inputted integer to 1 for odd numbers and 0 for even numbers.
    if mod1 == 0: #If statment to determin if the modulus in 0 meaning it would be even.
        print("This integer is even.") #Print statment if integer is even.
    elif mod1 == 1: #If else statment to determine if the modulus is 1 meaning the integer would be odd.
        print("This integer is odd.") #Print statment if integer is odd.

    answer = input("Would you like to check another number? Enter yes or no:  ")  # at the end of the program it asks the user if they want to repeat the program.
    if answer not in ("yes", "no"): #If stament if answer is not yes/no
        print("Input not valid") # prints invalid input going back to the last step.
        break 
    if answer == "yes":  #If answer is yes this repeats the loop.
        continue
    else:
        input("\nPress the enter key to exit") #If answer is no this ends the program.
        break
