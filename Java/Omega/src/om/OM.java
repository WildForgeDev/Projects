
package om;

import Account.Account;
import Account.Services;
import Account.Supplies;
import java.util.ArrayList; // import the ArrayList class

public class OM {

    public static void main(String[] args) {
        ArrayList<Account> Acclist = new ArrayList<Account>(); // Create an ArrayList object to store accounts
        Supplies sup = new Supplies(12346, "Active", "John Smith",5,11.51); //Instantiate a new Supplies Object called sup and add attribute values
        Services ser = new Services(12347, "Active", "Jane Doe",11,13.53); //Instantiate a new Services Object called ser and add attribute values
        Acclist.add(sup); //Add sup object to ArrayList
        System.out.println("\n"); //New Line for readability
        Acclist.add(ser); //Add ser object to ArrayList
        System.out.println("\n"); //New Line for readability
        System.out.println("Number of Accounts: " + Acclist.size()); //Print ArrayList Size
        System.out.println("\n"); //New Line for readability
        System.out.println(Acclist);//Print Full Arraylist
        System.out.println("\n"); //New Line for readability
        Acclist.get(0).computeSales(); //Use computeSales Method on Arraylist
        System.out.println("\n"); //New Line for readability
        Acclist.get(1).computeSales(); //Use computeSales Method on Arraylist
        System.out.println("\n"); //New Line for readability
        System.out.println(Acclist.get(0)); // Test toString override
        System.out.println("\n"); //New Line for readability
        System.out.println(Acclist.get(1)); // Test toString override
        System.out.println("\n"); //New Line for readability
    }
}