<?php
class Person {
    
    // properties
    private $name;
    private $eyeColor;
    private $age;
    // static properties are properties set for the class itself not a specific object.
    public static $drinkingAge = 21;

    // Methods
    /*
    By using type delclaration, we can throw and error if wrong type is given.
    Works with:
    - class/interface names
    - self (used to reference the same class)
    - array
    - callable
    - bool
    - float
    - int
    - string
    - iterable
    - object
    */
    public function __construct($name, $eyeColor, $age){
        $this->name = $name;
        $this->eyeColor = $eyeColor;
        $this->age = $age;
    }

    // public function __destruct(){
        
    // }
     // static functions are functions set for the class itself not a specific object.
    public static function setDrinkingAge($newDA){
        self::$drinkingAge = $newDA;
    }

    public function getName(){
        echo $this->name;
    }

    public function getEyeColor(){
        echo $this->eyeColor;
    }

    public function getAge(){
        echo $this->age;
    }

    public function setName(string $name) {
        $this->name = $name;
    }

    public function setEyeColor(string $eyeColor) {
        $this->eyeColor = $eyeColor;
    }

    public function setAge(int $age) {
        $this->age = $age;
    }

    public function getDA(){
        return self::$drinkingAge;
    }
}

// class Pet extends Person{
//     public function owner() {
//         $a = $this->first;
//         return $a;
//     }
// }

?>