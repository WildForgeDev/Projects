package average;
// Import Scanner to get user input
import java.util.Scanner;

public class Average {
  public static void main(String[] args) {
    
// Create variables to store user input.
      float A1, A2, A3, A4;
      double cavg3;
     
// Store user input in created variables.      
    Scanner AV1 = new Scanner(System.in); // Create Scanner Object
    System.out.println("Enter 4 numbers you would like to average: ");
    A1 = AV1.nextInt();
    A2 = AV1.nextInt();
    A3 = AV1.nextInt();
    A4 = AV1.nextInt();
    AV1.close();
    
// Calculate average.
    cavg3 = (double) (A1+A2+A3+A4)/4;
    
// Print average.
    System.out.println ("The average of these numbers is: " + cavg3);
  }
}
