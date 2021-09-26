//: Playground - noun: a place where people can play

import UIKit

class Person {

    var name = ""
}
class BlogPost {
    
    var title:String?
    var body = "hey"
    var author:Person?
    var numberOfComments = 0

}

let post = BlogPost()

print(post.body + " hello!")

post.title = "yo"

// Optional Binding
if let actualTitle = post.title {
    print(actualTitle + " salut")
}

// Testing for nil
if post.title != nil {
    print(post.title! + " salut")
}
if post.title == nil {
    //Optional contains no value
}
