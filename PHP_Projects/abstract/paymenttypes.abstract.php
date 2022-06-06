<?php

abstract class Visa {
    public function visaPayment(){
        return "Perform a payment";
    }

// there needs to be a getPayment method in any class that uses this abstract class.

    abstract public function getPayment();
}

?>