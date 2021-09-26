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
# Traversals
    def preorder(self): # Create preorder method
        print(self.data) # Print root data value

        if self.left: #Traverse left nodes first
            self.left.preorder() # Print left most node

        if self.right: #Print Right node after left node
            self.right.preorder() #Print right node

    def inorder(self): #Create inorder method
        if self.left: #Traverse Left nodes
            self.left.inorder() 

        print(self.data) #Print Left Nodes First

        if self.right: # Print Right Nodes after Left Nodes
            self.right.inorder()
    
    def postorder(self):
        if self.left: #Traverse Left Print Node
            self.left.postorder()

        if self.right: #Traverse Right Node
            self.right.postorder()
        
        print(self.data) # Print Node


# Tree Structure
#         |100|
#       /       \
#    |60|      |110|
#   /    \    /    \
# |50|  |67||109|  |111| 
#
# Code Creating above structure.

root = Tree('100') # Set Root Node to 100
root.add_left('60')    # Set root node left child to 60
root.add_right('110')   # Set root node right child to 110
firstLeft = root.left # Set root node left child "60" to firstLeft variable
firstLeft.add_left('50') # Set firstLeft left child to 50
firstLeft.add_right('67') # Set firstLeft right child to 67
firstRight = root.right # Set root node right child "110" to firstRight variable
firstRight.add_left('109') # Set firstRight left child to 109
firstRight.add_right('111')  # Set firstRight right child to 111

#Traversals Output
print("Preorder Traversal:") # Print Output Label 
print(root.preorder()) # Call preorder method on root Tree
print("\n") # Print New Line for Readability 
print("Inorder Traversal:") # Print Output Label 
print(root.inorder()) # Call inorder method on root Tree
print("\n") # Print New Line for Readability 
print("Postorder Traversal:") # Print Output Label 
print(root.postorder()) # Call postorder method on root Tree