class OverloadingSum: # Create new class
    def _add_(self, other): # define the __add__ method in the OverloadingSum class
        if isinstance(self, set): #If the self object is a set, return the object and the other attribute.
            return self | other
        elif self == '4': #If self object equals 4 return the set of self and other.
            return '%s plus %s' % (self,other)
        self=self+other #create variable self and make it equal to self + other set.
        return self # return self object.

a = 4 #create variable a and set it to 4.
b = 5 #create variable b and set it to 5.
c = a + b #create variable c anmd set it to a + b.
print("4 + 5 = ", c, "is an example of using the + operator to add two integers,", a, "and", b,".") #print c variable.

list1 = (2,3,4) #create list and set it to variable list1
list2 = (5,6,7) #create list and set it to variable list2
listsum = list1 + list2 #create vsriable listsum and set it to the sum of list1 and list2.
print(listsum, "is an example of concatenating ", list1,"and", list2, ", into one list") #print listsum variable.

string1 = "This is a " #create string1 variable and assign a string to it.
string2 = "concatenated string." #create  string2 variable and assign a string to it.
addstrings = string1 + string2 #create addstrings variable and set it to the sum of string1 and string2.
print(addstrings, "is an example of concatenating", string1, "and", string2, " into one list.") #Print addstrings

result=OverloadingSum._add_("4", "3") #create result variable and set it to Overloading sum class and use the __add__ method on thje set of 2 and 3.
print(result + "is an example of overloading the __add__ method") #print result variable.
