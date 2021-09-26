
package sellitems;
import java.util.Scanner; // Import Scanner
import java.util.ArrayList; // import the ArrayList class
import java.text.*; //Import Java Text Format
public class SellItems { //Create Class

    public static void main(String[] args) {
         
        Scanner NewItem = new Scanner(System.in); // Create Scanner Object
        Scanner GetItems = new Scanner(System.in); // Create Scanner Object
        ArrayList<Float> Prices = new ArrayList<>(); // Create an ArrayList object
         
         
        while(true){ // Create While Loop to ask user for input.

         
        System.out.println("Please enter the item's price: "); // Get Item Price
        Prices.add(GetItems.nextFloat()); //Add items to arraylist
         
        // Ask user if they would like to input another item
        System.out.println("Would you like to enter the price of an item? Yes/No ");
        String answer = NewItem.nextLine();
        
        
        //Start if statment to see if user input = "No" to end while loop
            if (answer.equals("No")){
            double add; //Create variable to count items in arraylist
            add = 0; //Set initial count to 0.
            for(Float d : Prices) //For loop to iterat through and add prices
                add += d;
            double tax; // Create variable to calculate tax
            tax = add*.07;
            double fin = add + tax; //Create variable to calculate total price
            DecimalFormat df = new DecimalFormat("#.##"); // Add currency formatting
            System.out.println("The prices you entered were: "+Prices); //Print Arraylist
            System.out.println("Your subtotal without tax is $"+df.format(add)); //Print subtotal
            System.out.println("Your total tax is $"+df.format(tax)); //Pritn total tax
            System.out.println("Your total price plus tax is, $"+df.format(fin)); //Print total price plus tax
        break; //End loop
    }
        }
    }
    }