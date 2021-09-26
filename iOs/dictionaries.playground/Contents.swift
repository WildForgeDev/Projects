//: Playground - noun: a place where people can play

import UIKit



//Declaring a new dictonary
var carDB = [String:String]()

//Adding key value pairs
carDB["JSD 238"] = "Blue Ferrari"
carDB["SID 482"] = "Green Lamborghini"

//Retrieving Data
(carDB["ASD 238"])

// Update a value for a key
carDB["JSD 238"] = "Red Ferrari"

// Remove a key value pair
// carDB ["JSD 238"] = nil

// Iterate over it
for (license, car) in carDB {
    
    print("\(car) as a license: \(license)")
}
