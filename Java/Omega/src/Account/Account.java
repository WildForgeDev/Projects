//Packages
package Account;

//Imports
import java.util.Scanner; // Import Scanner

//Classes
public abstract class Account { //Create Abstract Class "Account"
    protected int accountId; //Add account ID Attribute to Account.
    protected String AccountActive; //Add account ID Attribute to Account.
    protected String OwnerName; //Add ownerName Attribute to Account.
    protected String accountType; //Add accountType Attribute to Account.
    protected double processingFee; //Add ownerName Attribute to Account.

//Constructor
public Account(int accountId){ //Create Constructor for Account Class
    super();
        this.accountId = accountId;}

//Setters
    public void setAccountId() { // Create setter for accountId attribute
        Scanner AccId = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please Enter this Account's ID?: ");
        int AcId = AccId.nextInt();
            this.accountId = AcId;}
    
    public void setAccountActive(String AccountActive) {
        Scanner AccAct = new Scanner(System.in); // Create Scanner Object
        System.out.println("Is this account active?: ");
        String answer = AccAct.nextLine();
        if (answer.equalsIgnoreCase("Yes")){
            this.AccountActive = "Active";
        
        }else if (answer.equalsIgnoreCase("No")){
              this.AccountActive = "Inactive";}
}
//Getters
    public int getAccountId() { // Create getter for accountId attribute
        return accountId;}

    public String getAccountActive() {
        return AccountActive;}

//Methods
    public abstract double computeSales(); //Create computeSales Abstract Method
}
    