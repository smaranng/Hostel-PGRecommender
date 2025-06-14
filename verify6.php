<?php
include('connect.php');

// Handle OTP submission
if (isset($_POST['submit'])) {
    $otp = $_POST['otp'];
    $userid=$_POST['userid'];
    $email=$_POST['email'];
    
    $query = "SELECT * FROM users WHERE  OTP = '$otp'";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) > 0) {
        // Verification is successful
        // Update the OTP to '0' in the database
        $sql = "UPDATE users SET OTP = '0' where User_Id='$userid' AND Email_id='$email'";
        $updateResult = mysqli_query($conn, $sql);

        if ($updateResult) {
            echo '<script>alert("OTP verified.");</script>';
    $redirectURL = "reset_password1.php? userid=" . $userid . "& email=" . $email;
    echo '<meta http-equiv="refresh" content="0.01;url=' . $redirectURL . '">';
            exit();  
        } else {
            echo 'Error updating OTP in the database.';
        }
    } else {
        echo '<script>
        alert("Invalid OTP. Please try again!!");
        window.history.back();
    </script>';
        
    }

    mysqli_close($conn);
}



