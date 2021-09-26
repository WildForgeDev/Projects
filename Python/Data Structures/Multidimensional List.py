def main(): #Intialize the program.
    doners = list(); # Create a list named donors.
    doners.append(list()) # Append statment to add information about donors in the list. 
    doners.append(list())
    doners.append(list())
    doners.append(list())
    for x in range(4): # Create for loop to loop through 4 iterations of user inputted donor information on the list
        doners[x].append(input('Name of doner:')) # Create loop starts with gathering user input for the donor names, email, telephone number, and charity name.
        doners[x].append(input('E-mail:'))
        doners[x].append(input('Telephone Number:'))
        doners[x].append(input('Charity:'))
    for i in range(4): # Create for loop  that starts an outer loop to iterate through each instance of a donor within the list.
        for j in range(4): # Create second for loop to print each of the attributes associated with each donor.
            print(doners[i][j]) # Print the attributes of each doners in the range of i and j.
            print (' ') # Add a line between each entry printed in the output.
    doners[1][0] = input ('change name to ') # Get user input for changing the information for the 2nd entry of the list for the name attribute.
    for i in range(4): # Create for loop  that starts an outer loop to iterate through each instance of a donor within the list.
        for j in range(4): # Create second for loop to print each of the attributes associated with each donor.
            print(doners[i][j]) # Print the updated list with the appended name inputed by thge user. 
main() # End Program