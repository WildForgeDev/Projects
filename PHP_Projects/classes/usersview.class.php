<?php

class UsersView extends Users{
    
    public function showUser($name){
        $results = $this->getUser($name);
        echo 'First Name: ' . $results[0]['users_firstname'] . '<br />';
        echo 'Last Name: ' . $results[0]['users_lastname'] . '<br />';
        echo 'Birthday: ' . $results[0]['users_dateofbirth'] . '<br />';
    }

}

?>