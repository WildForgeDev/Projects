//: Playground - noun: a place where people can play

import UIKit

class Person {

    var name = ""
}

class BlogPost {

    var title:String
    var body = "hey"
    var author:Person!
    var numberOfComments = 0
    
    init() {
        title = "My title"
        author = Person()
    }

    convenience init (customTitle:String) {
        self.init()
        title = customTitle
    }
}

let post = BlogPost(customTitle: "A custom title" )

