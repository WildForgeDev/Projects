def main():
    def SortByIncreasingLength(UserStringList): #Function defining the increaing length operation on the list.
        UserStringListIncLen = sorted(UserStringList, key=len,) #uses the sorted function and the length key to sort the list.
        return UserStringListIncLen

    def SortByDecreasingLength(UserStringList): #Function defining the decreasing length operation on the list.
        UserStringListDecLen = sorted(UserStringList, key=len, reverse=True) #uses the sorted function, the length key to sort the list and the reverse function to reverse the order.
        return UserStringListDecLen
    
    def SortByTheMostVowels(UserStringList): #Function to sort the list by the most vowels.
        UserStringListMaxVowels = sorted(UserStringList, key=lambda word: sum(ch in 'aeiou' for ch in word), reverse=True) # uses a sort by the lambda key to return the reverse of the list with the least vowels
        return UserStringListMaxVowels
        
    def SortByTheLeastVowels(UserStringList): #Function to sort the list by the least vowels.
        UserStringListMinVowels = sorted(UserStringList, key=lambda word: sum(ch in 'aeiou' for ch in word))# uses a sort by the lambda key to return the list with the least vowels
        return UserStringListMinVowels

    def CapitalizeEveryOtherCharacterInList(UserStringList): #Function captialize every other letter in the strings entered into the list.
            newList = []
            for word in UserStringList: #creates a new list and loops through the strings for manipulation of the strings.
                newList.append(CapitalizeEveryOtherCharacter(word))
            return newList

    def CapitalizeEveryOtherCharacter(Word): #Function captialize every other letter in the strings entered into the list.
            characters = list(Word)
            newList = []
            for index, character in enumerate (characters): #This loops through the characters of the strings in the list and based on therir rangfe position converts them to their
                if index % 2 == 0:                          #modulus equivilent and based on that position makes the charachter upper of lower giving us capitalization of every other character.
                  newList.append(character.lower())
                else:
                  newList.append(character.upper())
            return ''.join(newList)
    
    def ReverseWordOrdering(UserStringList): #Function to reverse the list order.
        UserStringListReverse = UserStringList[::-1] # Uses the slice to mirror the list or reverse it. Starts from the end and goes toward the beginning.
        return UserStringListReverse

    def FoldWordsOnMiddleOfListA(UserStringList): #Function to split the list equally into two new lists.
        foldlist = UserStringList # this was my clever way f splitting one function into two.
        x = len(foldlist)       # this creates a new list by taking the length of the list and dividing it in two and printing the new length of the string.
        y = int(x/2)
        a = [foldlist[0:y]]
        b = [foldlist[y:x]]
        return a
    def FoldWordsOnMiddleOfListB(UserStringList): #Function to split the list equally into two new lists.
        foldlist = UserStringList # This is part two of the splitting the list in two based on its range printing the second half.
        x = len(foldlist)
        y = int(x/2)
        a = [foldlist[0:y]]
        b = [foldlist[y:x]]
        return b

    UserStringList = [] # Defines an empty list container.
    while True:
        addstringornot = input("Would you like to add a new string? yes/no: ") #asks for user input to add a string to the list.
        if addstringornot == ("yes"): #Yes input appends the new string to the list.
            UserStringList.append(str(input("Please enter a string to add to the list: "))) #appending the list with a new string after a yes answer.
            continue
        elif addstringornot == ("no"): #If no answer is input by user the loop ends and breaks into the functions to be performed on the list.
            break
        else:
            input("Invalid Entry") #If an invalid entry is detected the loop skips the entry and starts at the beginning of the loop.
            continue
            
    print ("The list you entered is ",(UserStringList)) # these functions print the aformentioned function listed and explained above once the list of strings is compiled.
    print ("The list sorted by increasing length is ",(SortByIncreasingLength(UserStringList))) 
    print ("The list sorted by decreasing length is ",(SortByDecreasingLength(UserStringList))) 
    print ("The list sorted by the most vowels is ",(SortByTheMostVowels(UserStringList)))
    print ("The list sorted by the least vowels is ",(SortByTheLeastVowels(UserStringList)))
    print ("The list with every other letter capitalized is ",(CapitalizeEveryOtherCharacterInList(UserStringList)))
    print ("The list order reversed is ",(ReverseWordOrdering(UserStringList)))
    print ("The first half of the list is ",(FoldWordsOnMiddleOfListA(UserStringList)))
    print ("The second half of the list is ",(FoldWordsOnMiddleOfListB(UserStringList)))
main()
