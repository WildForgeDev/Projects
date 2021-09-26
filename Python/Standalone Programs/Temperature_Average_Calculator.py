def main():
    def ComputeAverageTemp(HourlyTemperatures): # This is my function for calculating the average of the user entered numbers.
        average = 0.0 # It works by defining th average as a float, iterates through the list, sums the total of all tempretures and divides them by the number of items in the list.
        for i in range(len(HourlyTemperatures)):
            average = HourlyTemperatures[i]+ average 
        average = average/len(HourlyTemperatures)
        return average

    def GetNumberFromUser(hour): #This function is used to get user input and works with the other functions to validate the user entry is valid.
        numberText = input("Please enter a temperature for hour " + str(hour) + ": ") #This converts all none integer entries to a null value ensuring blank and string entries do not crash the program.
        if numberText.lstrip("-").isdigit():
            return int(numberText)
        else:
            return None

    def PrintTemperatures(HourlyTemperatures): #This function creates the ending table showing the time and the corresponding user entry Temperature.
        print ("Hour    Temperature")  
        for i in range(len(HourlyTemperatures)):
            print(str(i)+":00    "+str(HourlyTemperatures[i]))

    HourlyTemperatures = [] #Declares the blank list to be filled with 24 tempreture entries for each hour of the day.
    i = 0
    while i < 24: #While loop iterates through the list appending each entry.
        number = GetNumberFromUser(i)
        if number == None:
            print("Invalid input") #Error handling that converts all none integer entries to a null value thus keeping the program from crashing.
        elif number < -50:
            print("Invalid input") #Error handling that converts all none integer entries to a null value thus keeping the program from crashing.
        elif number > 130:
            print("Invalid input") #Error handling that converts all none integer entries to a null value thus keeping the program from crashing.
        else:
            i=i+1
            HourlyTemperatures.append(number) #Statement appends the list once a valid user entry is recieved.
    print("The Average Temperature is ", ComputeAverageTemp(HourlyTemperatures)) # Calls the function to print the average for all entries in the list.
    print("Today's highest temperature is ", max(HourlyTemperatures)) #Prints the highest temperature recorded on the list.
    print("Today's lowest temperature is ", min(HourlyTemperatures)) #Prints the Lowest temperature recorded on the list.
    PrintTemperatures(HourlyTemperatures) #Calls function to print the table showing user entries and the time they correspond to
main()
