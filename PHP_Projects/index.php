<?php 

// declare(strict_types = 1);
include 'includes/autoloader.inc.php';
include_once "abstract/paymenttypes.abstract.php";
include_once "classes/BuyProduct.class.php";
include_once "classes/simpleclass.class.php";

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title></title>
    <style>
        * {background: black;}
        * {color: white;}
    </style>
</head>
<body>
    <?php 

    // $newperson = new Person('Chris', 'green', 31);
    
    // $newperson->getName();
    // echo '<br>';
    // $newperson->getEyeColor();
    // echo '<br>';
    // $newperson->getAge();

    // $newperson->setName('Lauren');
    // echo '<br>';
    // $newperson->getName();

// Static attributes/methods
    // echo Person::$drinkingAge;
    // Person::setDrinkingAge(18);
    // echo '<br>';
    // echo Person::$drinkingAge;
    // echo '<br>';
    // echo $newperson->getDA();
    // echo '<br>';

// this is an example of creating type errors if strict typing.
    // try{
    //     echo $newperson->setName(2);
    // } catch(TypeError $e){
    //     echo "Error!: " . $e->getMessage();
    // }

    // $newperson->getName();

    
    // $object = new NewClass;
    // unset($object);
    // echo $object->getProperty();


// abstract classes

    // $buyProduct = new BuyProduct();

    // echo $buyProduct->getPayment();

// Anonymous Classes 

// $obj = new SimpleClass();
// $obj->helloWorld();

// //anonymous class
// $newObj = new class(){
//     public function helloWorld() {
//         echo "<br />Hello World!";
//     }
// };

// $newObj->helloWorld();


// $testObj = new Test();
// $testObj->setUsersStmt('Jon', 'Lakey', '1994-04-06');

$userObj = new UsersView();
$userObj->showUser('Chris');

// $userObj2 = new UsersContr();
// $userObj2->createUser('Jack', 'Lakey', '1957-09-22');


    ?>
</body>
</html>