package sales;
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
    
public static class Supplies extends Account{ //Create Supplies Subclass of Account Class
    private int numberOfItemsSold; //Create numberOfItemsSold attribute
    private double pricePerItem; //Create pricePerItem attribute
    @Override //Override the computeSales method inherited from Accounts Class
    double computeSales(){
            DecimalFormat df = new DecimalFormat("$#.##"); // Add currency formatting
            double x =  numberOfItemsSold * pricePerItem;
            System.out.println("Total Supplies Sales: " + df.format(x));
            return x;
    }
    //Create constructor for Supplies Subclass
    public Supplies(int accountId, int numberOfItemsSold, double pricePerItem){
        super(0);
        this.accountId = accountId;
        this.numberOfItemsSold = numberOfItemsSold;
        this.pricePerItem = pricePerItem;
    }
    
// Create setter for NumberOfItemsSold attribute
        public void setNumberOfItemsSold(int numberOfItemsSold) {
            if (numberOfItemsSold <= 0 )
            this.numberOfItemsSold = 0;
         else {
                this.numberOfItemsSold = numberOfItemsSold;}    
        }
        
// Create setter for PricePerItem attribute
        public void setPricePerItem(double pricePerItem) {
            if (pricePerItem <= 0 )
            this.pricePerItem = 0;
         else {
                this.pricePerItem = pricePerItem;}
        }
        
// Create getter for NumberOfItemsSold attribute
        public int getNumberOfItemsSold() {
            return numberOfItemsSold;
        }
// Create getter for PricePerItem attribute
        public double getPricePerItem() {
            return pricePerItem;
        }
//Override toString Method for Supplies Subclass
        @Override
        public String toString(){
        return ("Account Id: " + accountId + " " + "\nItems sold:" + " " + numberOfItemsSold + " " + "\nPrice Per Item: $" + pricePerItem);}
    }
    
    
    public static class Services extends Account{ // Create Services Subclass of Account Class
        private int numberOfHours; // Create numberOfHours attribute
        private double ratePerHour; // Create ratePerHour attribute
        
        @Override //Override the computeSales method inherited from Accounts Class
        double computeSales(){
            DecimalFormat df = new DecimalFormat("$#.##"); // Add currency formatting
            double x =  numberOfHours * ratePerHour;
            System.out.println("Total Services Sales: " + df.format(x));
            
            return x;
    }
        //Create constructor for Supplies Subclass
        public Services(int accountId, int numberOfHours, double ratePerHour){
        super(0);
        this.accountId = accountId;
        this.numberOfHours = numberOfHours;
        this.ratePerHour = ratePerHour;
    }
// Create setter for numberOfHours attribute
        public void setNumberOfHours(int numberOfHours) {
            if (numberOfHours <= 0 )
            this.numberOfHours = 0;
         else {
                this.numberOfHours = numberOfHours;}
        }
        
// Create setter for ratePerHour attribute
        public void setRatePerHour(double ratePerHour) {
            if (ratePerHour <= 0 )
            this.ratePerHour = 0;
         else {
                this.ratePerHour = ratePerHour;}
        }
        
// Create getter for numberOfHours attribute
        public int getNumberOfHours() {
            return numberOfHours;}
        
// Create getter for RatePerHour attribute
        public double getRatePerHour() {
            return ratePerHour;}
        
//Override toString Method for Services Subclass
        @Override
        public String toString(){
        return ("Account Id: " + accountId +" " + "\nNumber of Hours:" + " " + numberOfHours + " " + "\nHourly Rate: $" + ratePerHour);}
}
    
}
