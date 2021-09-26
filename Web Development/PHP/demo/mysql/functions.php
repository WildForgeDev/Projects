<?php


include "db.php";

function encrypt_password($password){
    $hash_format = '$2y$10$';
    $salt = "5M7eGyHkDuLbHtbkdzpqux";
    $hash_and_salt = $hash_format . $salt;
    $encrypt_password = crypt($password, $hash_and_salt);
    return $encrypt_password;
}

function clean($conn, $input){
    $input = mysqli_real_escape_string($conn, $input);
    return $input;
}

function get_all_users(){
    global $conn;
    $query = "SELECT * FROM users";
    $result = mysqli_query($conn, $query);
    if(!$result){
        die('QUERY FAILED:');
    }
    while($row = mysqli_fetch_assoc($result)){
        $id = $row['id'];
        echo "<option value='$id'>$id</option>";    
    }
}



function create_user(){
    global $conn;
    if(isset($_POST['submit'])){
        $username = $_POST['username'];
        $password = $_POST['password'];
        $username = clean($conn, $username);
        $password = clean($conn, $password);
        $password = encrypt_password($password); 
        $query = "INSERT INTO users(username, password) 
                  VALUES('$username', '$password')";
        $result = mysqli_query($conn, $query);
        if(!$result){
            die("Query failed");
        } else {
            echo "<br></br>";
            echo "User created!";
            echo "<br></br>";
        }
    }
}


function read_users(){
    global $conn;
        if($conn){
            echo "You are connected";
        } else{
            die("Connection Failed");
        }
    $query = "SELECT * FROM users";
    $result = mysqli_query($conn, $query);
    if(!$result){
        die("Query failed");
    } else {
        echo "<br></br>";
        echo "Users found!";
        echo "<br></br>";
    }
    return $result;
}


function update_user(){
    global $conn;
    if(isset($_POST['submit'])){
        $username = $_POST['username'];
        $password = $_POST['password'];
        $username = clean($conn, $username);
        $password = clean($conn, $password);
        $password = encrypt_password($password); 
        $id = $_POST['id'];
        $query = "UPDATE users 
                  SET username = '$username', password = '$password'
                  WHERE id = $id";
        $result = mysqli_query($conn, $query);
        if(!$result){
            die("QUERY FAILED!" . mysqli_error($conn));
        } else {
            echo "<br></br>";
            echo "User updated!";
            echo "<br></br>";
        }
    }
}


function delete_user(){
    global $conn;
    if(isset($_POST['submit'])){
        $id = $_POST['id'];
        $query = "DELETE 
                  FROM users
                  WHERE id = $id";
        $result = mysqli_query($conn, $query);
        if(!$result){
            die("QUERY FAILED!" . mysqli_error($conn));
        } else {
            echo "<br></br>";
            echo "User deleted!";
            echo "<br></br>";
        }
    }
}

function read_user_table($result){
    while($row = mysqli_fetch_assoc($result)){
        echo "<tr>";
        echo "<td>" . $row['username']. "</td>";
        echo "<td>" . $row['password']. "</td>";
        echo "</tr>";
        echo "<br></br>";
        print("<pre>".print_r($row, true)."</pre>");
    }
}


?>