<?php
class NewClass{
    
    //properties go here.
    public $data = "I am a property";

    //methods go here.
    public function __construct(){
        echo "This object has been instantiated.";
    }

    public function setNewProperty($newdata){
        $this->data = $newdata;
    }

    public function getProperty(){
        return $this->data;
    }

    public function __destruct(){
        echo "<br> This is the end of the class!";
    }
}

?>

