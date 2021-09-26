def bubbleSort(myArray): # Create bubbleSort function and pass in the array.
    num = int(input("Enter number of elements in the array: ")) # Get size of array
    for i in range (0, num): # Iterate through length of array and get user input for elements to fill array.
        print("Enter a number to add to the array: ")
        ent = int(input())
        myArray.append(ent)

def swapElement(myArray): # Create swapElement function and pass in array.
    for i in range (0, len(myArray) - 1): # Outer Loop to Iterate through the elements of array.
        for j in range(0, len(myArray) - 1 - i): # Inner Loop to swap larger elements with smaller for elements that come after.
            if myArray[j] > myArray[j+1]: # Continue to next element and continue swapping elements.
                myArray[j], myArray[j+1] = myArray[j + 1], myArray[j]

def printArray(myArray): #Create printArray function to print the sorted array.
    print ("The sorted array is:", myArray)
    

def main(): # Create Main function.
    myArray = [] # Create Array to store elements.
    bubbleSort(myArray) # Run bubbleSort function on array.
    swapElement(myArray) # Run swapElement funtion on array.
    printArray(myArray) # Run printArray function on array.

main() # End Program.
