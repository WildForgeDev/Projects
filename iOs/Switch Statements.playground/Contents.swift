//: Playground - noun: a place where people can play

import UIKit

var someCharacter:Character = "c"

switch someCharacter {
    
    case "a":
        print ("is an A")
    
    case "b", "c":
        print ("is a B or C")
    
    default:
        print("some fallback")
}
