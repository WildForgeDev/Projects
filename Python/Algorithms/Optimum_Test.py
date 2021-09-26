# Dynamic Programming code for Optimal Binary Search  
# Tree Problem  
  
INT_MAX = 2147483647
  
""" A Dynamic Programming based function that 
calculates minimum cost of a Binary Search Tree. """
def optimalSearchTree(keys, freq, n): 
  
    """ Create an auxiliary 2D matrix to store 
        results of subproblems """
    cost = [[0 for x in range(n)]  
               for y in range(n)] 
  
    """ cost[i][j] = Optimal cost of binary search  
    tree that can be formed from keys[i] to keys[j].  
    cost[0][n-1] will store the resultant cost """
  
    # For a single key, cost is equal to 
    # frequency of the key  
    for i in range(n): 
        cost[i][i] = freq[i]  
  
    # Now we need to consider chains of  
    # length 2, 3, ... . L is chain length.  
    for L in range(2, n + 1): 
      
        # i is row number in cost  
        for i in range(n - L + 2): 
              
            # Get column number j from row number  
            # i and chain length L  
            j = i + L - 1
            if i >= n or j >= n: 
                break
            cost[i][j] = INT_MAX 
              
            # Try making all keys in interval  
            # keys[i..j] as root  
            for r in range(i, j + 1): 
                  
                # c = cost when keys[r] becomes root  
                # of this subtree 
                c = 0
                if (r > i): 
                    c += cost[i][r - 1] 
                if (r < j): 
                    c += cost[r + 1][j] 
                c += sum(freq, i, j)  
                if (c < cost[i][j]): 
                    cost[i][j] = c 
    return cost[0][n - 1]  
  
  
# A utility function to get sum of  
# array elements freq[i] to freq[j]  
def sum(freq, i, j): 
  
    s = 0
    for k in range(i, j + 1): 
        s += freq[k]  
    return s  
      
# Driver Code 
if __name__ == '__main__': 
    keys = [10, 12, 20] 
    freq = [34, 8, 50] 
    n = len(keys) 
    print("Cost of Optimal BST is", 
           optimalSearchTree(keys, freq, n))