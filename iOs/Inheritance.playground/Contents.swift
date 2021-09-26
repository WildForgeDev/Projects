//: Playground - noun: a place where people can play

import UIKit

class Car {
    
    var topSpeed = 200
    
    func drive() {
        print("Driving at \(topSpeed)")
    }
}

class Futurecare : Car {
    
    override func drive() {
        
        super.drive()
        print ("and rockets boosting at 50")
    }
    
    func fly() {
        print("Flying")
    }

}

let myRide = Car()
myRide.topSpeed
myRide.drive()

let myNewRide = Futurecare()
myNewRide.topSpeed
myNewRide.drive()
myNewRide.fly()
