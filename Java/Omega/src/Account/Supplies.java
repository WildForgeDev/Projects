//Packages
package Account;

//Imports
import java.text.DecimalFormat;
import java.util.Scanner;

//Classes
public class Supplies extends Account{ //Create Supplies Subclass of Account Class
    private int numberOfItemsSold; //Create numberOfItemsSold attribute
    private double pricePerItem; //Create pricePerItem attribute
    
//Constructor
    //Create Supplies Constructor
    public Supplies(int accountId, String AccountActive, String OwnerName, int numberOfItemsSold, double pricePerItem){
        super(0);
        this.accountId = accountId;
        this.AccountActive = AccountActive;
        this.OwnerName = OwnerName;
        this.accountType = "Supplies Account";
        this.numberOfItemsSold = numberOfItemsSold;
        this.pricePerItem = pricePerItem;
        this.processingFee = 50.25;
    }
    
//Setters
    public void setNumberOfItemsSold(int numberOfItemsSold) {
        Scanner SetNumIS = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please enter the number of items sold for this account.: ");
        int SNIS = SetNumIS.nextInt();
            this.numberOfItemsSold = SNIS;}
        
    public void setPricePerItem(double pricePerItem) {
            Scanner SetPricePI = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please enter the price per item for this account.: ");
        int SPPI = SetPricePI.nextInt();
            this.pricePerItem = SPPI;}

    public void setOwnerName(String OwnerName) {
        Scanner SetOwnN = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please enter the account owner name: ");
        String Son = SetOwnN.nextLine();
        this.OwnerName = Son;}
   
    public void setprocessingFee(String processingFee) {
        Scanner SetProF = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please enter the account processing fee: ");
        int SPF = SetProF.nextInt();
        this.processingFee = SPF;}
        

// Getters
    public int getNumberOfItemsSold() {
        return numberOfItemsSold;}

    public String getOwnerName() {
        return OwnerName;}

    public String getClientType() {
        return accountType;}

    public double getprocessingFee() {
        return processingFee;}
    
   
//Overrides (Example of polymorphism for computing sales in ArrayList)
    @Override 
    public double computeSales(){
            DecimalFormat df = new DecimalFormat("$#.##"); // Add currency formatting
            double x =  numberOfItemsSold * pricePerItem;
            System.out.println("Total Supplies Sales: " + df.format(x));
            return x;}
//Override toString Method
    @Override
    public String toString(){
        return ("Account Id: " + accountId + "\nAccount Status: " + AccountActive + "\nAccount Owner: " + OwnerName + "\nAccount Type: " + accountType + "\nItems sold:" + " " + numberOfItemsSold + " " + "\nPrice Per Item: $" + pricePerItem + "\nAccount Processing Fee: $" + processingFee);}
}
