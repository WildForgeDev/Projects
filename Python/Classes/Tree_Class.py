class Tree: # Create Tree Class
    def __init__(self, data): #Create Constructor
        self.data = data # Node value attribute
        self.left = None # Node right pointer attribute
        self.right = None # Node Left pointer atribute
    
    def add_left(self, data): # create add_left node method
        if self.left == None: # if left attribute of node is null
            self.left = Tree(data) # Create new left node and set pointer to node value
        else: 
            newnode = Tree(data) # newnode variable equals new node data value.
            newnode.left = self.left # newnode left value equals left attribute pointer
            self.left = newnode # left attribute pointer equals newnode variable
    
    def add_right(self, data): # create add_left node method
        if self.right == None: # if right attribute of node is null
            self.right = Tree(data) # Create new right node and set pointer to node value
        else:
            newnode = Tree(data) # newnode variable equals new node data value.
            newnode.right = self.right # newnode left value equals left attribute pointer
            self.right = newnode # left attribute pointer equals newnode variable
# Node Structure

#    |3|
#   /   \
# |2|   |4|
#          \
#          |6|
#         /   \
#       |5|  |10|

root = Tree('3') # Set Root Node to 3
root.add_left('2')    # Set root node left child to 2
root.add_right('4')   # Set root node right child to 4

firstLevel = root.right # Set root node right child "4" to firstLevel variable
firstLevel.add_right('6') # Set firstLevel right child to 6

secondLevel = firstLevel.right # Set firstLevel right child to secondLevel variable
secondLevel.add_left('5') # Set secondLevel left child to 5
secondLevel.add_right('10')  # Set secondLevel right child to 10

thirdLevel = secondLevel.right # Set secondLevel right child to thirdLevel variable

print(root.data) # Print Root Node
print(firstLevel.data) # Print firstLevel (root node right child)
print(secondLevel.data) # Print secondLevel (firstLevel right child)
print(thirdLevel.data) # Print thirdLevel (secondLevel right child)