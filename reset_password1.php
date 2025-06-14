<!DOCTYPE html>
<html>
<head>
    <title>Reset Password</title>
    <style>
        body {
            background: linear-gradient(to bottom right, rgb(18, 102, 101), rgb(59, 130, 123), rgb(80, 153, 147), rgb(119, 139, 205));
            opacity: 0.8;
            text-align: center;
        }
        .container {
            margin: 100px auto;
            width: 350px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            font-size: 17px;
        }
        h2 {
            font-size: 25px;
            color: #333;
        }
        input[type="text"], input[type="password"],input[type="number"],input[type="email"] {
            width: 85%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        input[type="submit"] {
            width: 60%;
            padding: 13px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        .show-password-label {
            display: block;
            text-align: left; /* Align the checkbox to the left */
            font-size: 16px; /* Reduce the font size */
        }
        .show-password-checkbox {
            margin-right: 5px; /* Add a small margin to the checkbox */
        }
    </style>
</head>
<body>
<div class="container">
    <h2>Reset Password</h2>
    <form action="verify7.php" method="post">
        <br>
        User Id:<input type="text" id="userid" name="userid" class="form-control" value="<?php echo isset($_GET['userid']) ? $_GET['userid'] : ''; ?>" readonly>
               <br>
        Email Id:<input type="email" id="email" name="email" class="form-control" value="<?php echo isset($_GET['email']) ? $_GET['email'] : ''; ?>" readonly>
               <br>
        New Password: <input type="password" name="password" id="password" placeholder="Enter New Password" required>
        <br>
        Confirm Password:<input type="password" name="cpassword" placeholder="Confirm Password" required>
        <br>
        <br>
        <label class="show-password-label" for="showPassword">
            <input type="checkbox" id="showPassword" class="show-password-checkbox" onclick="togglePasswordVisibility()">
            Show Password
        </label><br><br>
        <input type="submit" name="submit" value="Reset Password">
        <br><br>
    </form>
</div>
<script>
function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}
</script>
</body>
</html>
