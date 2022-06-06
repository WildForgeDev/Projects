<?php

class Users extends Dbh{

    protected function getUser($name){
        $sql = "SELECT * FROM users where users_firstname = ?";
        $stmt = $this->connect()->prepare($sql);
        $stmt->execute([$name]);

        $results = $stmt->fetchAll();
        return $results;
    }

    protected function setUser($first_name, $last_name, $dob){
        $sql = "INSERT INTO users (users_firstname, users_lastname, users_dateofbirth) VALUES (?, ?, ?)";
        $stmt = $this->connect()->prepare($sql);
        $stmt->execute([$first_name, $last_name, $dob]);
    }
    

}

?>