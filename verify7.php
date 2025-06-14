<?php
include('connect.php');
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize the input
    $email=$_POST['email'];
    $newPassword = $_POST['password'];
    $confirmPassword = $_POST['cpassword'];
    $userid=$_POST['userid'];
    

    if ($newPassword === $confirmPassword) {
        // Passwords match, proceed with password reset and database update

        // Replace with the appropriate SQL query to update the password // Replace with the actual user ID
        $hashedPassword = password_hash($newPassword, PASSWORD_BCRYPT);

        $updateQuery = "UPDATE users SET Password = '$hashedPassword' WHERE User_Id = '$userid' AND Email_id='$email' ";

        if ($conn->query($updateQuery) === TRUE) {
            // Password updated successfully, redirect to the next page
            echo '<script>alert("Your Password has been reset successfully!!")
            window.location.href = "Login.php";</script>';
        } else {
            echo '<script>alert("Password Reset failed!")
            window.location.href = "Login.php";</script>';
        }

        // Close the database connection
        $conn->close();
    } else {
        echo '<script>
        alert("Passwords do not match!!!");
        window.history.back();
    </script>';
    }
}
$conn->close();
?>
