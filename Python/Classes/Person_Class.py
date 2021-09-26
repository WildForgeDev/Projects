def main():
    def ComputeAverageTemp(HourlyTemperatures):
        average = 0.0
        for i in range(len(HourlyTemperatures)):
            average = HourlyTemperatures[i]+ average 
        average = average/len(HourlyTemperatures)
        return average

    def GetNumberFromUser(hour):
        numberText = input("Please enter a temperature for hour " + str(hour) + ": ")
        if numberText.isdigit():
            return int(numberText)
        else:
            return None

    def ValidRange(number):
        return number < -50 or number > 130

    def PrintTemperatures(HourlyTemperatures):
        print ("Hour    Temperature")  
        for i in range(len(HourlyTemperatures)):
            print(str(i)+":00    "+str(HourlyTemperatures[i]))
    

    HourlyTemperatures = []
    i = 0
    while i < 24:
        number = GetNumberFromUser(i)
        if number == None:
            print("Invalid input")
        else:
            i=i+1
            HourlyTemperatures.append(number)
    print("The Average Temperature is ", ComputeAverageTemp(HourlyTemperatures))
    PrintTemperatures(HourlyTemperatures)
main()
