<?php

class Signup extends Dbh2{

    protected function checkUser($uid, $email){
        $stmt = $this->connect()->prepare('SELECT users_id FROM users WHERE users_uid = ? OR users_email = ?;');
        if(!$stmt->execute(array($uid, $email))){
            $stmt = null;
            header("location: ../index2.php?error=stmtfailed");
            exit();
        }
        $resultCheck = false;
        if($stmt->rowCount() > 0){
            $resultCheck = false;
        } else {
            $resultCheck = true;
        }
        return $resultCheck;
    }

    protected function setUser($uid, $pwd, $email){
        $stmt = $this->connect()->prepare('INSERT INTO users (users_uid, users_pwd, users_email) VALUES (?, ?, ?);');
        
        $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

        if(!$stmt->execute(array($uid, $hashedPwd, $email))){
            $stmt = null;
            header("location: ../index2.php?error=stmtfailed");
            exit();
        }
        $stmt = null;
    }

}

?>