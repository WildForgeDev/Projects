//Packages
package Account;

//Imports
import java.util.Scanner; // Import Scanner
import java.text.*; // Import java.text

//Classes
public class Services extends Account{ // Create Services Subclass of Account Class
        private int numberOfHours; // Create numberOfHours attribute
        private double ratePerHour; // Create ratePerHour attribute
    
//Constructors
//Create Services Constructor
public Services(int accountId, String AccountActive, String OwnerName, int numberOfHours, double ratePerHour){
    super(0);
        this.accountId = accountId;
        this.AccountActive = AccountActive;
        this.OwnerName = OwnerName;
        this.accountType = "Service Account";
        this.numberOfHours = numberOfHours;
        this.ratePerHour = ratePerHour;
        this.processingFee = 100.55;}
//Setters
        //Example of data hiding
        public void setNumberOfHours(int numberOfHours) {
        Scanner SetNumH = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please Enter the number of service hours for this account.: ");
        int Snh = SetNumH.nextInt();
            this.accountId = Snh;}
        
        public void setRatePerHour(double ratePerHour) {
            Scanner SetRateH = new Scanner(System.in); // Create Scanner Object
        System.out.println("Please Enter the service hourly rate for this account.: ");
        int Srh = SetRateH.nextInt();
            this.accountId = Srh;}
               
        public void setOwnerName(String OwnerName) {
            Scanner SetOwnN = new Scanner(System.in); // Create Scanner Object
            System.out.println("Please Enter the Account Owner Name: ");
            int Son = SetOwnN.nextInt();
            this.accountId = Son;}  
        
        public void setprocessingFee(String processingFee) {
            Scanner SetProF = new Scanner(System.in); // Create Scanner Object
            System.out.println("Please enter the account processing fee: ");
            int SPF = SetProF.nextInt();
            this.processingFee = SPF;}
        
//Getters
        public int getNumberOfHours() {
            return numberOfHours;}
        
        public double getRatePerHour() {
            return ratePerHour;}

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
            double x =  numberOfHours * ratePerHour;
            System.out.println("Total Services Sales: " + df.format(x));      
                return x;}
//Override toString Method
        @Override
            public String toString(){
                    return ("Account Id: " + accountId + "\nAccount Status: " + AccountActive + "\nAccount Owner: " + OwnerName + "\nAccount Type: " + accountType + "\nNumber of hours: " + " " + numberOfHours + " " + "\nRate per hour: $" + ratePerHour + "\nAccount Processing Fee: $" + processingFee);}
}