structure = {'A': ['B', 'C'], 'B':['D', 'E'], 'C':['D','E'], 'D':['E'],'E': ['A']} #Create Node structure as dictionary
fullPath = [] #Create list as fullpath variable

def recursiveDFS (structure, nodeStart, fullPath): #Create function for depth first analysis with structure, nodeStart, fullPath parameters
    fullPath = fullPath + [nodeStart]  #set fullpath variable to fullpath plus the starting node
    print (fullPath)    #Print full path variable
    for node in structure[nodeStart]: # create for loop to cycle throgh the node structure
        if not node in fullPath:           # If a node has not been visited then add it to and return the full path.
            fullPath = recursiveDFS(structure, node, fullPath)   
    return fullPath
print ('Recursive Depth First Search Result', recursiveDFS(structure, 'A', fullPath)) #Call and print depth first function

def iterativeBFS(structure, nodeStart, fullPath): # Create function for breadth first analysis as dictonary with structure, nodeStart, fullPath parameters    
    x = [nodeStart]    #Set variable X equal to node start
    while x:      #Create while loop to start at node start and print the node start
        print(x)        
        firstNode = x.pop(0) #Create first node variable and pop all nodes visited from the list
        if not firstNode in fullPath:            
            fullPath = fullPath + [firstNode]           
            x = x + structure[firstNode]    
    return fullPath #Return the path taken to traverse through the tree.
print('Iterative Breadth First Search Result', iterativeBFS(structure, 'A', fullPath)) # Call and print the breadth first function