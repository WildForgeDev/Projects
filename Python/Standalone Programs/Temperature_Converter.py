#===================================================================

#    CS119T – Unit 1-Submission Node – Convert Fahrenheit to Celsius

#    Filename: Unit 1 Submission Node: my-unit1-submission-node.doc

#    Author: Christopher Lakey

#    Purpose:   Demonstrate basic Python programming in the IDLE

#               development environment

#               by following steps 1 through 6 above.

#===================================================================

while True:
    print("Fahrenheit to Celsius Converter")

    ftemp = float(input("Please enter the Fahrenheit temperature you wish to be converted to Celsius: ")) # Prompt for user to enter Fahrenheit temperature to be converted to Celcius.

    x = 32.0 # Defining integer needed in first operation to be subtracted from user Fahrenheit entry to start Celcius conversion.

    y = 5.0 # Defining first integer needed in second operation for temperature conversion.

    z = 9.0 # Defining second integer needed in second operation for temperature conversion.

    firstcalc = ftemp - x # First operation needed to convert Celsius Fahrenheit.

    seccalc = y / z # Second operation needed to convert Celsius Fahrenheit.

    ctemp = seccalc * firstcalc # Third and final operation needed to convert user provided Fahrenheit temperature to Celsius temperature.

    print(ftemp, "degrees Fahrenheit converts to", ctemp, "degrees Celsius.") # Shows the user the result of temperature conversion.

    answer = input("Would you like to convert another temperature? key yes/no: ") # Statement asking user if they would like to convert another temperature.

    if answer not in ("yes", "no"): # Statement that handles non yes/no inputs.
        print("Input not valid")
        break

    if answer == "yes": # Reiterates the program when user answers yes to converting another temperature.
        continue
    else:
        input("\nPress the enter key to exit") # Exits the program when user does not want to convert another temperature.
        break        
