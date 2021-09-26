import UIKit

//
// CodeWithChris Learn Swift for Beginners
// http://codewithchris.com/learn-swift
//
// Challenge #1: The Lost Animal Challenge
//
// Instructions: 
// Given the two arrays below, write a function that takes a String as an input parameter and returns a Boolean value. The function should return true if the String input is in either array and it should return false if the String input is in neither array.
//
// Examples:
// Call your function and pass in the String "cat" as the input. Your function should return true
// Call your function and pass in the String "cow" as the input. Your function should return false
 
let array1 = ["dog", "cat", "bird", "pig"]
let array2 = ["turtle", "snake", "lizard", "shark"]

// Write your function below:

// Start Function
func test(animal:String) -> Bool {
// Combine lists
let list = array1 + array2
// Loop through list to find animal
    for item in list {
        if item == animal {
            return true;
        }
    }
//looped through every item and didnt find the animal.
//returning false
    return false;
}
let result1 = test(animal: "cat")
let result2 = test(animal: "cow")

print(result1)
print(result2)
