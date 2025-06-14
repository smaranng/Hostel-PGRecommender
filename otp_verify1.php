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
        body {
            background: linear-gradient(to bottom right, rgb(18, 102, 101), rgb(59, 130, 123), rgb(80, 153, 147), rgb(119, 139, 205));
            text-align: center;
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
        input[type="email"],input[type="text"],input[type="number"] {
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
    <div class="container">
        <h2>OTP Verification</h2>
        <br>
        <form action="verify6.php" method="post">
            <label for="userid"><b>User Id:</b></label>
            <input type="text" id="userid" name="userid" class="form-control" value="<?php echo isset($_GET['userid']) ? $_GET['userid'] : ''; ?>" readonly>
               <br>
               <label for="email"><b>Email Id:</b></label>
               <input type="email" id="email" name="email" class="form-control" value="<?php echo isset($_GET['email']) ? $_GET['email'] : ''; ?>" readonly>
               <br><label for="otp"><b>OTP:</b></label>
               <br>
            <input type="number" name="otp" placeholder="Enter OTP" required>
            <br><br>
            <input type="submit" name="submit" value="Verify">
            <br><br><br>
        </form>
    </div>
</body>
</html>
