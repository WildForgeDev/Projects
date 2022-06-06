<?php
// Interfaces - This creates a ruleset that a group of classes should follow in order to handle multiple objects.

interface PaymentInterface{
    public function paymentProcess();
}

interface LoginInterface{
    public function paymentProcess();
}

class Paypal implements PaymentInterface, LoginInterface{
    public function payNow(){}
    public function loginFirst(){}
    public function paymentProcess(){
        $this->loginFirst();
        $this->payNow();
    }
}

class Visa implements PaymentInterface{
    public function payNow(){}
    public function paymentProcess(){
        $this->payNow();
    }
}

class Cash implements PaymentInterface{
    public function payNow(){}
    public function paymentProcess(){
        $this->payNow();
    }
}

class BankTransfer implements PaymentInterface, LoginInterface{
    public function payNow(){}
    public function loginFirst(){}
    public function paymentProcess(){
        $this->loginFirst();
        $this->payNow();
    }
}

class BuyProduct{
    public function pay(PaymentInterface $paymentType){
        $paymentType->paymentProcess();
    }
}

$paymentType = new Cash();
$buyProduct = new BuyProduct();
$buyProduct->pay($paymentType);

?>