<?php
    $fullname =$_POST['fullname'];
    $email=$_POST['email'];

    $conn = new mysqli('localhost,'root','','test');
    if($conn->connect_error){
        die('connection failed :'.$conn->connection_error);
    }else{
        $stmt = $conn->prepare("insert into sign(fullname,email)
            values(?,?)")
        $stmt->bind_param("ss",$fullname,$email)
        $stmt->execute();
        echo "done dana don";
        $stmt->close();
        $conn->close();
    }
?>