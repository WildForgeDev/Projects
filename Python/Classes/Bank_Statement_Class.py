from Transaction import Transaction
# BankStatement Class
class BStatement:    
    # Declaring the constructor   
    def __init__(self, initialBal=0.0):       
        self.__BeginningBal = initialBal      
        self.__EndingBal = initialBal      
        self.__TransactionLog = []        
        self.__ArrangedLog = []        
        self.__RunningBalLog = []        
        self.__NumberofEntries = 0        
        self.__NumberofDeposits = 0        
        self.__NumberofWithdrawals = 0
# Setter for beginning and end balance
    
    def setBegEndBals(self, BegEndBalance):    
        self.__BeginningBal = self.__EndingBal = BegEndBalance
# Getter for beginning balance
    
    def getBeginningBal(self):   
        return self.__BeginningBal
# Getter for end balance
    
    def getEndingBal(self):   
        return self.__EndingBal
# Getter for the number of entries
    
    def getNumberofEntries(self):   
        return self.__NumberofEntries
# Getter for the number of deposits
    
    def getNumberofDeposits(self):    
        return self.__NumberofDeposits
# Getter for the number of withdrawals
    
    def getNumberofWithDrawals(self):   
        return self.__NumberofWithdrawals
# Insert transaction method
    
    def insertTransaction(self, transaction):    
        self.__TransactionLog.append(transaction)   
# Appending this transaction to the transaction log    
        self.__NumberofEntries += 1  
# Incrementing the number of entries
# If there is a deposit then we add the amount to last amount
        if transaction.getCode() == 'Deposit':    
            self.__NumberofDeposits += 1 
# Incrementing the number of deposits    
# if RunningBalLog is not empty get the last balance and add amount    
            if len(self.__RunningBalLog) > 0:      
                    self.__EndingBal = self.__RunningBalLog[-1] + transaction.getAmount()        
                    self.__RunningBalLog.append(self.__EndingBal)  
# Appending the end balance to running balance log    
            else:        
                # Otherwise, it means its the first transaction      
                    self.__EndingBal = self.getBeginningBal() + transaction.getAmount()        
                    self.__RunningBalLog.append(self.__EndingBal)
        else:  
            # otherwise there is a withdrawal transaction, for example:
            # deduct the amount       
            self.__NumberofWithdrawals += 1        
        if len(self.__RunningBalLog) > 0:           
                self.__EndingBal = self.__RunningBalLog[-1] - transaction.getAmount()            
                self.__RunningBalLog.append(self.__EndingBal)       
        else:           
                self.__EndingBal = self.getBeginningBal() - transaction.getAmount()            
                self.__RunningBalLog.append(self.__EndingBal)
# Displaying all transactions, beginning and end balances
    def displayResults(self):    
        print("The beginning transaction was: $" + str(self.__BeginningBal))
        for index, t in enumerate(self.__TransactionLog):    
            print("Transaction: " + str(index + 1) + " was a " + t.getCode() + " amount: $" + str(t.getAmount()) + " for " + t.getNote())   
            print("Running Bal: $" + str(self.__RunningBalLog[index]))
        print("The ending balance is: $" + str(self.__EndingBal))
        print("The number of Transactions are: " + str(self.__NumberofEntries)) #The number of transactions are printed
        print("The number of Deposits are: " + str(self.__NumberofDeposits)) 
# The number of Deposits are printed
        print("The number of Withdrawals are: " + str(self.__NumberofWithdrawals)) 
# The number of Withdrawals are printed
# Arranging the current transactions
    
    def arrangeTransactions(self):    
        self.__ArrangedLog.clear()  
# Clearing the current list    
# Then, loop through all of the transactions. Also, add all 
# deposit transactions   
        for t in self.__TransactionLog:        
            if t.getCode() == 'Deposit':            
                self.__ArrangedLog.append(t)    
# Loop through all of the transactions and then finally add 
# all of the withdrawal transactions   
        for t in self.__TransactionLog:        
            if t.getCode() == 'Withdrawal':         
                self.__ArrangedLog.append(t)
# Prints the arranged transactions    
    
    def printArranged(self):        
        print("Printing the Deposits and Withdrawals as a group:")        
        for index, t in enumerate(self.__ArrangedLog):            
            print("Transaction was a " + t.getCode() + " amount: $" + str(t.getAmount()) + " for " + t.getNote())
# Start method to be called from main method


def start():
    myStatement = BStatement()    
    myStatement.setBegEndBals(29.92)
    T1 = Transaction()   
    T1.setAmount(157.56)    
    T1.setCode('Deposit')
    T1.setNote('CTPay')
    T2 = Transaction(149.86, 'Withdrawal', "Rent")
    T3 = Transaction()
    T3.setAmount(89.56)
    T3.setCode('Deposit')
    T3.setNote('Tips')
    T4 = Transaction(17.56, 'Deposit', "Gift")
    T5 = Transaction()
    T5.setAmount(89.77)
    T5.setCode('Withdrawal')
    T5.setNote('Date')
    T6 = Transaction(167.75, 'Deposit', "Loan")
    T7 = Transaction()
    T7.setAmount(90.00)
    T7.setCode('Withdrawal')
    T7.setNote('Loan Payment')
    T8 = Transaction(71.77, 'Withdrawal', "Groceries")
    myStatement.insertTransaction(T1)
    myStatement.insertTransaction(T2)
    myStatement.insertTransaction(T3)
    myStatement.insertTransaction(T4)
    myStatement.insertTransaction(T5)
    myStatement.insertTransaction(T6)
    myStatement.insertTransaction(T7)
    myStatement.insertTransaction(T8)
    myStatement.displayResults()
    myStatement.arrangeTransactions()
    myStatement.printArranged()
    # Main method of the program


if __name__ == '__main__':
    start()