//: Playground - noun: a place where people can play

import UIKit

class Person {
    
    var name = ""
}

class BlogPost {
    
    // Computed property
    var fulltitle:String {
        
        //Check that title and author are not nil
        if title != nil && author != nil {
            return title! + " by " + author!.name
        }
        else if title != nil {
            return title!
        }
        else {
            return "No Title"
        }
    }
    
    var title:String?
    var body = "hey"
    var author:Person?
    var numberOfComments = 0

}

let author = Person()
author.name = "Chris Lakey"

let myPost = BlogPost()
print(myPost.fulltitle)

