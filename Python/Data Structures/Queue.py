class Queue: #Create Queue Class
    def __init__(self):
        self.customerNames = [] # Create list to store queue items

    def isempty(self): #Create Method to empty queue
        return self.customerNames == []

    def enqueue (self, customername): # Create Enqueue Method to add names to the end of the queue.
        self.customerNames.append(customername)
    
    def dequeue(self): # Create Method to remove the first name in the queue
        if len(self.customerNames) < 1:
            return None
        return self.customerNames.pop(0)

    def size(self): # Create method to get size of the queue
        return len(self.customerNames)
    
    def front(self): # Create Method to get the first name in the queue.
        return self.customerNames[0]
    
    def end(self): #  Create Method to get the last name in the queue.
        return self.customerNames[-1]

q = Queue() # Create Queue object
q.enqueue('Bonnai') # Add Bonnai to front of queue
q.enqueue('Tim') # Add Tim to end of queue
q.enqueue('Jerry') # Add Jerry to end of queue
q.enqueue('Tom') # Add Tom to end of queue
print ("Queue Size: ", (q.size())) # Print current Queue Size
print(q.front(), "is at the front of the queue") # Print first name in Queue
print(q.end(), "is at the end of the queue") # Print last name in Queue
print(list(q.customerNames)) # Print all names in the Queue
q.dequeue() # Remove Bonnai to front of queue
q.dequeue() # Remove Tim from front of the queue
print ("Queue Size: ", (q.size())) # Print current Queue Size
print(q.front(), "is at the front of the queue") # Print first name in Queue
print(q.end(), "is at the end of the queue") # Print last name in Queue
