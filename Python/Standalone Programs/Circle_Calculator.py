import math # This statement inporths the Python Math Library
def main(): 
    rad = float(input("Enter radius of the circle: ")) # Creates a user input for the circle radius.
    print("The diameter of the circle is: %.2f" % (rad * 2)) # Prints the diameter of the circle from the user input radius
    print("The circumference of the circle is: %.2f" % (2 * math.pi * rad)) # Prints the circumference of the circle from the user input radius
    print("The area of the circle is: %.2f" % (math.pi * rad ** 2)) # Prints the area of the circle from the user input radius

main()
