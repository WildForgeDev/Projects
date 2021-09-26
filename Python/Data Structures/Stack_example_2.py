def main():
    garage = list()
    for i in range(0,5):
        garage.append(input("What is the model of the car you are parking in the garage? "))
    car = input("Which car model is yours? " "Car model: ")
    number =  0
    while garage.pop() != car:
        number += 1
    estimate = (number+1) * 5
    print("It will take",estimate,"minutes in order to retrieve your car") 
main()