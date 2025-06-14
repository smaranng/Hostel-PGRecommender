<?php
// Include the database connection file
include('connect.php');

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get and sanitize the school code and password
    $userid = mysqli_real_escape_string($conn, $_POST['userid']);
    $password = mysqli_real_escape_string($conn, $_POST['passwordInput']);

    // Check if the school is registered
    $checkSchoolQuery = "SELECT User_Id, Password, Name FROM users WHERE User_Id = ?";
    $stmt = $conn->prepare($checkSchoolQuery);
    $stmt->bind_param("s", $userid);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $hashedPassword = $row['Password'];
        // Verify the password
        if (password_verify($password,$hashedPassword)) {
            // Password is correct, allow access or redirect to the school's dashboard
            session_start();
            $name = $row['Name'];
            $_SESSION['name'] = $name;
            
            // Display the alert message using JavaScript
            echo '<script>
                    alert("Login Successful!!");
                    window.location.href = "http://127.0.0.1:5000";
                  </script>';
            exit();
            

        } else {
            // Incorrect Password
            echo '<script>
                alert("Incorrect Password!");
                window.location.href = "Login.php";
            </script>';
        }
    } else {
        // School not registered
        echo '<script>
            alert("User not yet registered!");
            window.location.href = "index.php";
        </script>';
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}
?>
