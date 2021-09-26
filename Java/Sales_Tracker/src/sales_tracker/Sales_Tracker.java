package sales_tracker;
 
import Account.Account.Supplies;
import Account.Account.Services;

public class Sales {

   
    public static void main(String[] args) { 
        Supplies sup = new Supplies(12346,5,11.51); //Instantiate a new Supplies Object called sup and add attribute values
        System.out.println(sup); //Test toString override
        sup.computeSales(); //Test computeSales Method for Supplies Subclass
        //Test using the setter for accountId and set it to invalid entry.
        sup.setAccountId(900);
        //Test using the setter for numberOfItemsSold and set it to invalid entry.
        sup.setNumberOfItemsSold(-8);
        //Test using the setter for pricePerItem and set it to invalid entry.
        sup.setPricePerItem(-20);
        System.out.println(sup.getAccountId()); // test getter for accountId
        System.out.println(sup.getNumberOfItemsSold()); // test getter for numberOfItemsSold
        System.out.println(sup.getPricePerItem()); // test getter for PricePerItem
        sup.computeSales(); //Test computeSales Method for Supplies Subclass
        System.out.println("\n"); //New Line for readability
        
        Services ser = new Services(12347,11,13.53); //Instantiate a new Services Object called ser and add attribute values
        System.out.println(ser); //Test toString override
        ser.computeSales(); //Test computeSales Method for Supplies Subclass
        //Test using the setter for accountId and set it to invalid entry.
        ser.setAccountId(900);
        //Test using the setter for numberOfHours and set it to invalid entry.
        ser.setNumberOfHours(-10);
        //Test using the setter for RatePerHour and set it to invalid entry.
        ser.setRatePerHour(-20);
        System.out.println(ser.getAccountId()); // test getter for accountId
        System.out.println(ser.getNumberOfHours()); // test getter for numberOfHours
        System.out.println(ser.getRatePerHour()); // test getter for RatePerHour
        ser.computeSales(); //Test computeSales Method for Supplies Subclass
        System.out.println("\n"); //New Line for readability
    }
    
}