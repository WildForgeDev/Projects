# Create Node Class
class studentnode(object):
    def __init__(self, i, a = None):
        self.info = i # Node info variable
        self.contnode = a # Continue to next node variable
    def getnextnode (self): # get next node
        return self.contnode
    def new_next (self, a): # set the next node
        self.contnode = a
    def get_info (self): # Get node info
        return self.info
    def set_info (self, i): # Set Node info
        self.info = i

#Create Linked List Class 
class LinkedList(object):
    def __init__(self, b = None):
        self.root = b
        self.size = 0
    def takesize (self): # Get list size
        return self.size
    def addnewnode (self, i): # Add Node to root
        nnode = studentnode (i, self.root)
        self.root = nnode
        self.size += 1
    def delete (self, i): # Delete node and set previous node to deleted node's next node.
        currentnode =self.root
        lastnode = None
        while currentnode:
            if currentnode.get_info() == i:
                if lastnode:
                    lastnode.new_next(currentnode.getnextnode())
                else:
                    self.root = currentnode
                self.size -= 1
                return True # Delete info
            else:
                lastnode = currentnode
                currentnode = currentnode.getnextnode()
        return False # Cannot locate info
    def locate (self, i): # locate new next node and get it.
        currentnode = self.root
        while currentnode:
            if currentnode.get_info() == i:
                return i
            else:
                currentnode = currentnode.getnextnode()
        return None
    def deleteall (self):
        temp = self.root
        if temp is None:
            print("\n Not possible to delete empty list")
        while temp:
            self.head = temp.getnextnode()
            temp = None
            temp = self.root
            print("Linked list contains no data")
            break
        #test = self.root
        #lastnode = None
        #test = lastnode
    
    def printNode(self):
        node1 = self.root
        while node1:
            print(node1.info)
            node1 = node1.getnextnode()

        


# List Actions
newlist = LinkedList() # Create linked list object named new list
newlist.addnewnode(2) # Add new node
newlist.addnewnode(7) # Add new node
newlist.addnewnode(19) # Add new node
newlist.addnewnode(11) # Add new node
newlist.addnewnode(35) # Add new node
newlist.delete(35) # Delete Node
print(newlist.delete(35)) # Print if node was deleted
print(newlist.locate(19)) # Locate "19" node
print(newlist.locate(2)) # Locate "2" node
print(newlist.size) # Print Linked List size
newlist.printNode()
newlist.deleteall()
newlist.printNode()
