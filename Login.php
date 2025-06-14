<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title>Login page</title>
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<link rel="stylesheet" href="style2.css">
<style>
/* CSS Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    width: 100%;
    height: 100%;
    overflow: hidden;
}

#preloader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.preloader-content {
    text-align: center;
    position: relative;
}

.circle {
    position: absolute;
    border: 4px solid transparent;
    border-radius: 100%;
    animation: spin 2s linear infinite;
}

.circle:nth-child(2) {
    width: 30px;
    height: 30px;
    top: -20px;
    left: -20px;
    border-top-color: #ff5e3a;
    animation: spin 1.5s linear infinite;
}

.circle:nth-child(3) {
    width: 70px;
    height: 70px;
    top: -40px;
    left: -40px;
    border-top-color: #ffcc00;
    animation: spin 2s linear infinite;
}

.circle:nth-child(4) {
    width: 110px;
    height: 110px;
    top: -60px;
    left: -60px;
    border-top-color: #006400;
    animation: spin 2.5s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>
</head>
<body>
<div id="preloader">
    <div class="preloader-content">
        <div class="circle circle1"></div>
        <div class="circle circle2"></div>
        <div class="circle circle3"></div>
        <div class="circle circle4"></div>
    </div>
</div>

<img src="logo1.jpg" style="position: absolute; top: 75px; left: 740px; width: 60px; height: 60px;">
<h1 style="margin-left: 800px; position: absolute; top: 75px; color: white; font-size: 40px;">PG and Hostel Tracker</h1>
<div class="center">
    <div class="loginbox">
        <img src="2.png" class="avatar">
    </div>
    <br>
    <h1>Login</h1>
    <form action="Connection2.php" method="post" onsubmit="return validateForm()">
        <div class="input-box">
            <span class="icon">
                <ion-icon name="person"></ion-icon>
            </span>
            <input type="text" name="userid" id="userid" required>
            <label>User_Id</label>
        </div>
        <div class="input-box">
            <span class="icon">
                <ion-icon name="lock-closed"></ion-icon>
            </span>
            <input type="password" id="passwordInput" name="passwordInput" required>
            <span></span>
            <label>Password</label>
        </div>
        <br>
        <div class="input box">
            <label><input type="checkbox" id="showPasswordCheckbox"> Show Password</label>
            <br><br>
            <div class="pass" align="right">
                <a href="forgot_password1.php">Forgot Password?</a>
            </div>
        </div>
        <br>
        <input type="submit" name="submit" value="Login">
        <br>
        <div class="image">
            <img src="pgh.webp" alt="Image">
        </div>
    </form>
</div>

<script>
function validateForm() {
    var selectedRole = document.getElementById("select").value;

    if (selectedRole == "select") {
        alert("Please select a valid role to Login (Administrator, Teacher, or Principal).");
        return false; 
    }
    return true; 
}

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("passwordInput");
    const showPasswordCheckbox = document.getElementById("showPasswordCheckbox");

    if (showPasswordCheckbox.checked) {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

const showPasswordCheckbox = document.getElementById("showPasswordCheckbox");
showPasswordCheckbox.addEventListener("click", togglePasswordVisibility);

var loader = document.getElementById("preloader");
setTimeout(function() {
    loader.style.display = "none";
}, 5000);
</script>
</body>
</html>
