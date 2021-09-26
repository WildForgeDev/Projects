class Students: # Create class students
    def __init__(self): # Use init constructor to build the self object
        self.studentName = None # Create the student name attribute
        self.studentEmailaddress = None # Create the student email attribute
        self.studentID = None # Create the student ID attribute
        self.tuitonBalance = None # Create the tuition balance attribute
    def setstudentName(self,studentName): #Create function with the self object and the student name variable.
        self.studentName=studentName  #Set the self object attribute to be the student name variable
    def setstudentEmailaddress(self,studentEmailaddress): #Create function with the self object and the student email variable.
        self.studentEmailaddress=studentEmailaddress #Set the self object attribute to be the student email variable
    def setstudentID(self,studentID): #Create function with the self object and the studentID variable.
        if len(studentID)==6:  # Test if the integer length of the student ID is equal to six.
            self.studentID=studentID #If student ID is equal to 6 return true.
            return True
        else: #if student ID is not equal to 6 (returning false) print the message to enter the student ID again.
            print("Student ID# must be six digits. try again. ")
            return False 
    def settuitionBalance(self,tuitionBalance): #Create function with the self object with the variable tuitionBalance.
        if int(tuitionBalance) > 0: #If tuition balance integer is greater than 0 return True
            self.tuitonBalance = tuitionBalance
            return True 
        else: #If the tuition balance variable integer is less than 0 return false and print message to re-enter the tuition amount.
            print("A student's tuition balance cannnot be negative. ")
            return False
    def printStudents(self): #Create function for self object to print the selected students information.
        print(self.studentName, "with email",self.studentEmailaddress,"and ID number",self.studentID,"owes tuition of $",self.tuitonBalance)
students = list() #create list with the name students to store student data.
for i in range(0,4): #Create loop to get student data.
    tempor = Students()
    tempor.setstudentName(input("Enter student's name: "))
    tempor.setstudentEmailaddress(input("Enter student's Email address: "))
    while not tempor.setstudentID(input("Enter the student's ID number: ")):
        print("Enter the student's ID number again: ") #While loop to re-iterate through invalid responses to Student ID number user entry.
    while not tempor.settuitionBalance(input("Enter the student's tuition balance: ")):
        print("Enter the student's tuition balance again: ") #While loop to re-iterate through invalid responses to tuition balance user entry.
    students.append(tempor) #Append list with user entered data.
checkStudent = input("Which student would you like to look at?") #Get user input for which student information user wants to display.
for i in range(0,4): # Create for loop to look through lists data for matching student name.
    if students[i].studentName == checkStudent: #If student name matches user entry display user data from list.
        students[i].printStudents() 


