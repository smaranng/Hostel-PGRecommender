<!DOCTYPE html>
<html>
<head>
    <title>Forgot Password</title>
    <style>
    body {
        background: url('S.jpeg') no-repeat;
        background-size: cover;
        text-align: center;
        margin: 0;
        padding: 0;
    }

    #preloader {
        background: white url(785.gif) no-repeat center center;
        width: 99%;
        height: 100%;
        top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
        position: fixed;
        z-index: 1000;
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
    input[type="password"] {
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
<div id="preloader"></div>
    <div class="container">
        <h2>Forgot Password</h2>
        <form action="verify2.php" method="post">
            <input type="text" name="schoolCode" placeholder="Enter School Code" required>
            <br><br>
            <input type="text" name="email" placeholder="Enter Email" required>
            <br>
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
