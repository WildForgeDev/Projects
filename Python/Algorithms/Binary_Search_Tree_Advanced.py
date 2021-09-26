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
    def preorder(self):
        print(self.data)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()
        
        print(self.data)


# Tree Structure
#                  |8|
#                 /   \
#              |5|     |4|
#             /   \      \
#           |9|   |7|    |11| 
#                /   \
#              |1|   |12|
#                    /
#                  |2|
# Code Creating above structure.

root = Tree('8') # Set Root Node to 8
root.add_left('5')    # Set root node left child to 5
root.add_right('4')   # Set root node right child to 4

firstLeft = root.left # Set root node left child "5" to firstLeft variable
firstLeft.add_left('9') # Set firstLeft left child to 9
firstLeft.add_right('7') # Set firstLeft right child to 7

secondLeft = firstLeft.right # Set root node left child "7" to secondLeft variable
secondLeft.add_left('1') # Set secondLeft left child to 9
secondLeft.add_right('12') # Set secondLeft right child to 12

thirdLeft = secondLeft.right # Set root node left child "12" to thirdLeft variable
thirdLeft.add_left('2')

firstRight = root.right # Set root node right child "4" to firstRight variable
firstRight.add_right('11') # Set firstRight left child to 11

secondRight = firstRight.right # Set root node right child "4" to secondRight variable
secondRight.add_left('3') # Set secondRight left child to 3



print("Preorder Traversal:")
print(root.preorder())
print("\n")
print("Inorder Traversal:")
print(root.inorder())
print("\n")
print("Postorder Traversal:")
print(root.postorder())