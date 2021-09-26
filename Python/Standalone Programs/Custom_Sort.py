def main():
    def SortByIncreasingLength(UserStringList):
        UserStringListIncLen = sorted(UserStringList, key=len,)
        return UserStringListIncLen

    def SortByDecreasingLength(UserStringList):
        UserStringListDecLen = sorted(UserStringList, key=len, reverse=True)
        return UserStringListDecLen
    
    def SortByTheMostVowels(UserStringList):
        UserStringListMaxVowels = sorted(UserStringList, key=lambda word: sum(ch in 'aeiou' for ch in word), reverse=True)
        return UserStringListMaxVowels
        
    def SortByTheLeastVowels(UserStringList):
        UserStringListMinVowels = sorted(UserStringList, key=lambda word: sum(ch in 'aeiou' for ch in word))
        return UserStringListMinVowels

    def CapitalizeEveryOtherCharacter(UserStringList):
            newList = []
            for index, element in enumerate (UserStringList):
                if index %2 == 0
                
                newList.append(element.upper())
            return newList
    
    def ReverseWordOrdering(UserStringList):
        UserStringListReverse = UserStringList[::-1]
        return UserStringListReverse
    def FoldWordsOnMiddleOfListA(UserStringList):
        foldlist = UserStringList
        x = len(foldlist)
        y = int(x/2)
        a = [foldlist[0:y]]
        b = [foldlist[y:x]]
        return a
    def FoldWordsOnMiddleOfListB(UserStringList):
        foldlist = UserStringList
        x = len(foldlist)
        y = int(x/2)
        a = [foldlist[0:y]]
        b = [foldlist[y:x]]
        return b

    UserStringList = []
    while True:
        addstringornot = input("Would you like to add a new string? yes/no: ")
        if addstringornot == ("yes"):
            UserStringList.append(str(input("Please enter a string to add to the list: ")))
            continue
        elif addstringornot == ("no"):
            break
        else:
            input("Invalid Entry, Press enter to contine.")
            continue
    print ("The list you entered is "(UserStringList))
    print ("The list sorted by increasing length is "(SortByIncreasingLength(UserStringList)))
    print ("The list sorted by decreasing length is "(SortByDecreasingLength(UserStringList)))
    print ("The list sorted by the most vowels is "(SortByTheMostVowels(UserStringList)))
    print ("The list sorted by the least vowels is "(SortByTheLeastVowels(UserStringList)))
    print ("The list order reversed is "(ReverseWordOrdering(UserStringList)))
    print ("The first half of the list is "(FoldWordsOnMiddleOfListA(UserStringList)))
    print ("The first half of the list is "(FoldWordsOnMiddleOfListB(UserStringList))
    print (CapitalizeEveryOtherCharacter(UserStringList))
main()

