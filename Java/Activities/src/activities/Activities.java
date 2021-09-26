
package activities;
import java.util.Scanner; // Import Scanner

public class Activities {  //create activities class

    public static void main(String[] args) { //create main method

        Scanner WhatDay = new Scanner(System.in); // Create Scanner Object
        Scanner AskDay = new Scanner(System.in); // Create Scanner Object
    while(true){ //start while loop to ask user if they want to look up activities.
        System.out.println("Would you like to check tha specific weekday's activities? ");
        String answer2 = AskDay.nextLine();
        if (answer2.equalsIgnoreCase("Yes")){ //if statement if user wants to look at a day's activites
        
            System.out.println("Please enter a day of the week to see the activities for that day: "); // get user input
            String answer = WhatDay.nextLine(); //store user input
            if (answer.equalsIgnoreCase("Monday")){ //iterate through if statments to find the specific day to print activity
                System.out.println("Monday's activity is baseball.");
                continue;
      }     else if (answer.equalsIgnoreCase("Tuesday")){
                System.out.println("Tuesday's activity is football.");
                continue;
      }     else if (answer.equalsIgnoreCase("Wednesday")){
                System.out.println("Wednesday's activity is painting.");
                continue;
      }     else if (answer.equalsIgnoreCase("Thursday")){
                System.out.println("Thursday's activity is woodworking.");
                continue;
      }     else if (answer.equalsIgnoreCase("Friday")){
                System.out.println("Friday's activity is guitar class.");
                continue;
      }     else if (answer.equalsIgnoreCase("Saturday")){
                System.out.println("Saturday's activity is hiking.");
                continue;
      }     else if (answer.equalsIgnoreCase("Sunday")){
                System.out.println("Sunday's activity is biking.");
                continue;
      }     else System.out.println("That is not a valid day of the week.");//If a day is not entered inform user and repeat loop
                continue;
  }     else;    //if user enters no then the program ends
        break;
}
    }
}
