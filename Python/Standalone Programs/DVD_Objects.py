def display_dvd_information(dvds):  # Create function to display dvd title, cost, and type
    for obj in dvds:  # Create loop to print the list of dvds
        print(obj.title)
        print(obj.dvd_type)
        print(obj.cost)


def display_total_and_average_cost(dvds):  # Create function
    add = 0  # starting value for total dvd cost and average is 0
    for obj in dvds:  # Loop through all DVDs
        add += obj.cost  # Add each DVD's cost to total.
    print(obj.cost)  # Print the total DVD cost.
    avg = add/len(dvds)  # Calculate average of dvd cost
    print('Average cost: ', avg)  # Print calculated average


def change_dvd(dvd):  # Create function
    print('DVD title is', dvd.title)  # Print DVD title
    in1 = input('Do you want to change the DVD title? (y/n: ')  # Ask for user input to change the dvd title
    if in1 in ['y', 'Y']:  # If user input is y or Y then get user input for new title
        title = input('Enter new title: ')
        dvd.title = title  # Newly entered title is changed to title attribute
    else:  # if user does not want to change title then move to next statement
        pass
    print('This DVD type is', dvd.dvd_type)  # Print DVD type
    in2 = input('Do you want to change the DVD type? (y/n): ')  # Ask for user input to change the dvd type
    if in2 in ['y', 'Y']:  # If user input is y or Y then get user input for new dvd type
        valid_type = ['Game', 'Word', 'Compiler', 'Spreadsheet', 'Dbase', 'Presentation']  # State valid dvd types
        while True:  # While loop to get new dvd type
            dvd_type = input('Enter valid DVD type:')  # User input for new dvd type.
            if dvd_type.title() not in valid_type:  # If entered dvd type not a valid type do not change type.
                continue
            else:
                dvd.dvd_type = dvd_type  # if new dvd type is a valid type change type to new type.
            break
    else:  # If type is not changing move to next statement.
        pass
    print('The DVD cost is ', dvd.cost)  # Print DVD cost.
    in3 = input('Do you want to change the DVD cost? (y/n): ')  # get user input to change dvd cost.
    if in3 in ['y','Y']:  # if user input in y or Y format ask user to enter new cost.
        cost = int(input('Enter the new DVD cost:'))
        dvd.cost = cost  # new dvd cost is the cost
    else:   # if user did not change dvd cost then end the function.
        pass


class DVD(object):  # Create dvd class
    def __init__(self, title, dvd_type, cost):  # define the self object and title, type, and cost attributes.
        self.title = title  # title attribute of self object is equal to title variable.
        self.dvd_type = dvd_type  # type attribute of self object is equal to type variable.
        self.cost = cost  # cost attribute of self object is equal to cost variable.

    def set_title(self, new_title):  # Define set title method for DVD object
        self.title = new_title  # Title attribute equals the new title variable

    def get_title(self):  # Define get title method for DVD object.
        return self.title  # Return the title attribute of self object

    def set_dvd_type(self,new_dvd_type):  # Define set type method for DVD object
        self.dvd_type = new_dvd_type  # type attribute equals the new type variable

    def get_type(self):  # Define get type method for DVD object.
        return self.dvd_type  # Return the type attribute of self object

    def set_cost(self, new_cost):  # Define set cost method for DVD object
        self.cost = new_cost  # cost attribute equals the new type variable

    def get_cost(self):  # Define get cost method for DVD object.
        return self.cost  # Return the cost attribute of self object

    def list_valid_dvd_types(self):  # Define list valid dvd types method for DVD object.
        valid_type = ['Game', 'Word', 'Compiler', 'Spreadsheet', 'Dbase', 'Presentation']  # List valid dvd types
        if self.dvd_type.title() in valid_type:  # if the dvd type is a valid type in the DVD object
            return True  # Return true
        else:
            return False  # If not return false

    def load_information(self):  # Define load dvd information method for DVD object.
        title = input('Enter the dvd title: ')  # title variable equals user input to get dvd title.
        self.set_title(title)  # set the title to user input for title DVD object
        dvd_type = input('Enter the DVD type: ')  # type variable equals user input to get dvd type.
        self.set_dvd_type(dvd_type)  # set the type to user input for type DVD object
        cost = int(input('Enter the DVD cost: '))  # cost variable equals user input to get dvd cost.
        self.set_cost(cost)  # set the cost to user input for cost DVD object


def main():  # Define main program
    list1 = []  # Create list called list 1
    dvd1 = DVD('abd','xyz',100)  # Create dvd1 object and enter dvd name, type, and cost.
    dvd2 = DVD('abc', 'xyz', 100)  # Create dvd2 object and enter dvd name, type, and cost.
    dvd3 = DVD('abc', 'xyz', 100)  # Create dvd3 object and enter dvd name, type, and cost.
    dvd1.load_information()  # call load information method for dvd1 object
    list1.append(dvd1)  # append list1 with dvd1 object
    dvd2.load_information()  # call load information method for dvd2 object
    list1.append(dvd2)  # append list1 with dvd2 object
    dvd3.load_information()  # call load information method for dvd3 object
    list1.append(dvd3)  # append list1 with dvd3 object
    print('DVD information: ')  # Print DVD information and display information of list1
    display_dvd_information(list1)
    print('DVD costs: ')  # Print DVD cost and display total cost of list1
    display_total_and_average_cost(list1)
    for i in range(2):  # for loop for the dvds in the list1
        change_dvd(list1[i])  # Call change DVD function for list1
        print('Updated DVD information:')  # Print updated dvd information
        display_dvd_information(list1)  # Call display_dvd_information function

if __name__ == '__main__':  # if the program is being run directly then run the main program.
    main()
