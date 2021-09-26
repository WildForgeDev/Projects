package supertest;


import <any?>;
import java.text.DecimalFormat;

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
    
    