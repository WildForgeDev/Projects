class Node: #create the class node
    def __init__(self): # Use init constructor to add attributes to the Node class
        self.left = None #Create attribute left in the Node class and set it to null.
        self.right = None #Create attribute left in the Node class and set it to null.
        self.data = list() #Create attribute data to hold a list in the Node class

def addPerson(root, person): #Create Function with root and person variable
    if person < root.data[0]: #If Person’s last name is A-K (<0) they are added to the left attribute's list attribute in the node class.
        if root.left == None: 
            root.left = Node() #
            root.left.data.append(person)
        else:
            addPerson(root.left,person)
    else:
        if person > root.data[0]: #If Person’s last name is L-Z (>0) they are added to the Right attribute's list attribute in the node class.
            if root.right == None:
                root.right = Node()
                root.right.data.append(person)
            else:
                addPerson(root.right,person)
        else:
            root.data.append(person)
def printPerson(root): # Create function to print wedding guest list at the end of entering guest names.
    if root == None:
        return
    print(root.data)
    printPerson(root.left)
    printPerson(root.right)
    
root = Node() #Create variable for node class
root.data.append("L") #Add user input guest names to the root node data list attribute.
for i in range(0,6): #Create loop to iterate through getting user input for six guest names.
    addPerson(root,input("Please enter the wedding guest's name:")) #Get user input for guest names.
print("Left side of room A-K:") # Print the left nodes created to store guest names.
printPerson(root.left)
print("Right side of room L-Z:") # Print the right nodes created to store guest names.
printPerson(root.right)