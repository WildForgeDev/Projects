<?php

class CannedJob{
    function __construct($id, $name, $package_price){
        $this->id = $id;
        $this->name = $name;
        $this->package_price = $package_price;
        $this->labors = array();
        $this->parts = array();
    }

    function addLabor(Labor $labor){
        array_push($this->labors, $labor);
        return $this;
    }

    function addPart(Part $part){
        array_push($this->parts, $part);
        return $this;
    }

    function getPartsTotal(){
        $total = 0;
        foreach($this->parts as $part){
            $total += $part->getTotal(); 
        }
        return $total;
    }

    function getLaborTotal(){
        $total = 0;
        foreach($this->labors as $labor){
            $total += $labor->getTotal(); 
        }
        return $total;
    }

    function getTotal(){
        return $this->getPartsTotal() + $this->getLaborTotal();
    }

    function adjustPrices(){
        $parts_total = $this->getPartsTotal();
        $labor_total = $this->getLaborTotal();
        if($parts_total >= $this->package_price){
            foreach($this->parts as $part){
                $part->setTotal($part->getTotal() / $parts_total * $this->package_price);
            }
            foreach($this->labors as $labor){
                $labor->setTotal(0);
            }
        } else {
            foreach($this->labors as $labor){
                $labor->setTotal($labor->getTotal() / $labor_total * ($this->package_price - $parts_total));
            }
        }
        return $this;
    }
}


class Part{
    function __construct($id, $name, $price, $quantity, $tax_rate){
        $this->id = $id;
        $this->name = $name;
        $this->price = $price;
        $this->quantity = $quantity;
        $this->tax_rate = $tax_rate;
        $this->fees = array();
    }


    function getCharge(){
        return $this->price * $this->quantity;
    }


    function getTax(){
        return $this->getCharge() * $this->tax_rate;
    }

    function addFee(Fee $fee){
        array_push($this->fees, $fee);
        return $this;
    }

    function getTotal(){
        return round($this->getCharge() + $this->getTax() + $this->getFeesTotal(), 2);
    }

    function setTotal($total){
        $fee_total = $this->getFeesTotal();
        if($fee_total > $total) {
            $this->price = 0;
            foreach($this->fees as $fee){
                $fee->setTotal($fee->getTotal() / $fee_total * $total);
            }
        } else if ($this->getFeesTotal() == $total){
            $this->price = 0;
        } else {
            $this->price = ($total - $this->getFeesTotal()) / (1 + $this->tax_rate);
        }
        return $this;
    }

    function getFeesTotal(){
        $total = 0;
        foreach($this->fees as $fee){
            $total += $fee->getTotal();
        }
        return $total;
    }
}


class Labor{
    function __construct($id, $name, $hours, $rate, $tax_rate){
        $this->id = $id;
        $this->name = $name;
        $this->hours = $hours;
        $this->rate = $rate;
        $this->tax_rate = $tax_rate;
    }

    function setPrice($price){
        $this->rate = $price / $this->hours;
        return $this;
    }

    function getPrice(){
        return $this->rate * $this->hours;
    }

    function getTax(){
        return $this->getPrice() * $this->tax_rate;
    }


    function getTotal(){
        return round($this->getPrice() + $this->getTax(), 2);
    }

    function setTotal($total){
        $this->setPrice($total / (1 + $this->tax_rate));
        return $this;
    }
}


class Fee{
    function __construct($id, $name, $price, $tax_rate){
        $this->id = $id;
        $this->name = $name;
        $this->price = $price;
        $this->tax_rate = $tax_rate;
    }

    function getTax(){
        return $this->price * $this->tax_rate;
    }

    function getTotal(){
        return round($this->price + $this->getTax(), 2);
    }

    function setTotal($total){
        $this->price = ($total / (1 + $this->tax_rate));
        return $this;
    }
}

?>