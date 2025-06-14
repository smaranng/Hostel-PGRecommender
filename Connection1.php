<?php
include('connect.php');

if (isset($_POST['submit'])) {
    $user = mysqli_real_escape_string($conn, $_POST['user']);
    $userid = mysqli_real_escape_string($conn, $_POST['userid']);
    $phone = mysqli_real_escape_string($conn, $_POST['phone']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $school_Password = mysqli_real_escape_string($conn, $_POST['passwordInput']);
    $cschool_Password = mysqli_real_escape_string($conn, $_POST['cpasswordInput']);
    $state = mysqli_real_escape_string($conn, $_POST['inputState']);
    $district = mysqli_real_escape_string($conn, $_POST['inputDistrict']);

    $hash = password_hash($school_Password, PASSWORD_DEFAULT);

    $stmt = $conn->prepare("SELECT User_Id FROM users WHERE User_Id = ?");
    $stmt->bind_param("s", $userid); 
    $stmt->execute();
    $stmt->store_result(); 

    if($stmt->num_rows > 0) {
        echo '<script>alert("Data already exists"); window.location.href = "Register.php";</script>';
    } else {
        
        $insertQuery = $conn->prepare("INSERT INTO users (Name, User_Id, Phone_Number, Email_Id, Password, State, District) VALUES (?, ?, ?, ?, ?, ?, ?)");
        $insertQuery->bind_param("sssssss", $user, $userid, $phone, $email, $hash, $state, $district);

        if ($insertQuery->execute()) {
            echo '<script>alert("Registered Successfully"); window.location.href = "Login.php";</script>';
        } else {
            echo '<script>alert("Error while registering."); window.location.href = "Register.php";</script>';
        }

        $insertQuery->close(); 
    }

    $stmt->close(); 
}
?>
