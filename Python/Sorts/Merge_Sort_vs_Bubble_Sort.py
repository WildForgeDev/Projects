import sys # Import Modules
import timeit
import time
import datetime

# Create Two starting arrays for sorting.

start_array = [100, 45, 33, 55, 356, 11, 1000, 999, 987]
start_array_two = [100, 45, 33, 55, 356, 11, 1000, 999, 987]

# Define the bubble sort algorithm.
def bubble_sort(start_array_two):
    h = len(start_array_two)
 
    for i in range(h): # Iterate through Array
 
        # Compare two elements at a time until the largest are at the back of the array 
        for j in range(0, h - i - 1):
 
            # traverse the array from the beginning to end
            # Swap elements if the second element is greater
            # iterate to the next element.
            if start_array_two[j] > start_array_two[j+1] :
                start_array_two[j], start_array_two[j+1] = start_array_two[j+1], start_array_two[j]
    
# Define the merge sort algorithm.
def mergeSort(start_array):
    
    if len(start_array) > 1: 
        M = len(start_array)//2 # Split the array in half 
        L = start_array[:M] # Left side of the array
        R = start_array[M:]  # Right side of the array
  
        mergeSort(L) # Sort the left side of the array
        mergeSort(R) # Sort the right side of the array
  
        i = j = k = 0 # set iterator varibles to 0.
          
        # Move data to new split array.
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                start_array[k] = L[i] 
                i+=1
            else: 
                start_array[k] = R[j] 
                j+=1
            k+=1
          
        # Final iteration to see if any elements are not sorted.
        while i < len(L): 
            start_array[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            start_array[k] = R[j] 
            j+=1
            k+=1
    
    
# Function to print array one
def printList(start_array): 
    for i in range(len(start_array)):         
        print(start_array[i],end=" ") 
    print() 

# Function to print array two
def printListTwo(start_array_two): 
    for i in range(len(start_array_two)):         
        print(start_array_two[i],end=" ") 
    print()
  
# Main program to test the two sorting algorithms
if __name__ == '__main__':
# Testing the first Algorithm Merge Sort
    print (f"Given merge sort starting array is {start_array}")  
    start = timeit.default_timer()
    mergeSort(start_array)
    end = timeit.default_timer()
    time_one = end - start
    new_time_one = time_one * 1000
    print(f"After merge sorting, the array is: {start_array}") 
    print('The merge sort completed in {:03.3f}'.format(new_time_one),' milliseconds.')

# Testing the second Algorithm bubble Sort
    print (f"Given bubble sort starting array is {start_array_two}")
    start_two = timeit.default_timer()
    bubble_sort(start_array_two)
    end_two = timeit.default_timer()
    time_two = end_two - start_two
    new_time_two = time_two * 1000
    print(f"After bubble sorting, the array is: {start_array_two}")
    print('The bubble sort completed in {:03.3f}'.format(new_time_two),' milliseconds.')

# If statment that print's which algorithm was faster. 
    if new_time_one < new_time_two:
        print("Merge sort is the faster algorithm!!!")
    elif new_time_two < new_time_one:
        print("Bubble sort is the faster algorithm!!!")
    else:
        print(" There was an error.")
# End Program