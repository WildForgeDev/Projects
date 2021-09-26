class Stack: # Create Stack Class
    def __init__(self):
        self.bookIds = [] # Create BookId list to store the stack

    def isEmpty(self): # Create method to empty the stack
        return self.bookIds == []

    def push(self, bookId): # Create push Method to add a bookId to the top of the stack
        self.bookIds.insert(0,bookId)

    def pop(self): # Create pop method to remove the top item from the stack
        return self.bookIds.pop(0)
    
    def peek(self): #Create peek Method to view the item at the top of the stack.
        return self.bookIds[0] 

    def size(self): #Create Method to view the size of the stack.
        return len(self.bookIds)


x = Stack() # Create new stack object
x.push(1000) # Add 1000 to the top of the stack
x.push(2000) # Add 2000 to the top of the stack
x.push(3000) # Add 3000 to the top of the stack
x.push(4000) # Add 4000 to the top of the stack
print ("Stack Size: ", (x.size()))
print(x.peek(), "is at the top of the stack") # Print first name in Queue
print(list(x.bookIds)) # Print all names in the Stack
x.pop() # Remove the top item in the stack
x.pop() # Remove the top item in the stack
print ("Stack Size: ", (x.size()))
print(x.peek(), "is at the top of the stack") # Print first name in Queue
print(list(x.bookIds)) # Print all names in the Stack
x.pop() # Remove the top item in the stack
x.pop() # Remove the top item in the stack
print ("Stack Size: ", (x.size()))
print(list(x.bookIds)) # Print all names in the Stack