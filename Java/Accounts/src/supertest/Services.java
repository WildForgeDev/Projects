package supertest;

import java.text.DecimalFormat;
import supertest.Account.Services;
public class Services extends Account{ // Create Services Subclass of Account Class
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