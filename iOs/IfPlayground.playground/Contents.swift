//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

let a = 9
let b = 4
let c = 6

if (a < 4 || b < 4) && c != 3 {

    print("branch 1")
}
else if a < 8 {

    print("branch 2")
}
else if !(a == 10 && b == 1) {
    print ("branch 3")
}
else {
    print("nothing was true")
}
