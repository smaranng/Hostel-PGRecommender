<!DOCTYPE html>
<html>
<head>
    <title>Forgot Password</title>
    <style>
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

    body {
        text-align: center;
        margin: 0;
        background: linear-gradient(to bottom right, rgb(18, 102, 101), rgb(59, 130, 123), rgb(80, 153, 147), rgb(119, 139, 205));
        padding: 0;
        opacity: 0.8;
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

    input[type="text"],
    input[type="mail"] {
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
    <div class="container">
        <h2>Forgot Password</h2>
        <br>
        <form action="verify5.php" method="post">
            <input type="text" name="userid" placeholder="Enter User_Id" required>
            <br>
            <input type="mail" name="email" placeholder="Enter Email" required>
            <br>
            <br>
            <input type="submit" name="submit" value="Get OTP">
            <br><br>
        </form>
    </div>
    <script> 
 var loader=document.getElementById("preloader"); 
 setTimeout(function() {
     loader.style.display = "none";  }, 3000); 
</script>
</body>
</html>
