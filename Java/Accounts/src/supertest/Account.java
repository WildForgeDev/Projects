
package supertest;
import java.text.*; //Import Java Text Format

public abstract class Account { //Create Abstract Class "Account"
    
    protected int accountId; //Add account ID Attribute to Account.
    abstract double computeSales(); //Create computeSales Abstract Method
    
    public Account(int accountId){ //Create Constructor for Account Class
        super();
        this.accountId = accountId;
    }
    
    public void setAccountId(int accountId) { // Create setter for accountId attribute
        if (accountId <= 10000 || accountId >= 99999 )
            this.accountId = 00000;
         else {
                this.accountId = accountId;}
    }
    
    public int getAccountId() { // Create getter for accountId attribute
        return accountId;
    }               
    