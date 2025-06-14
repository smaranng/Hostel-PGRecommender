<?php
include('connect.php');
session_start();

$name = isset($_SESSION['name']) ? $_SESSION['name'] : "User";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/boxicons/2.0.7/css/boxicons.min.css">
    <title>Hostel & PG Tracker</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        /* Preloader styles */
        #preloader {
            position: fixed;
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

        .preloader-image {
            width: 60px;
            height: 60px;
            background: url('logo1.jpg') no-repeat center center;
            background-size: contain;
            margin-bottom: 20px;
            position: relative;
            z-index: 2;
        }

        .circle {
            position: absolute;
            border: 4px solid transparent;
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        .circle:nth-child(2) {
            width: 100px;
            height: 100px;
            top: -20px;
            left: -20px;
            border-top-color: #ff5e3a;
            animation: spin 1.5s linear infinite;
        }

        .circle:nth-child(3) {
            width: 140px;
            height: 140px;
            top: -40px;
            left: -40px;
            border-top-color: #ffcc00;
            animation: spin 2s linear infinite;
        }

        .circle:nth-child(4) {
            width: 180px;
            height: 180px;
            top: -60px;
            left: -60px;
            border-top-color: #00ffcc;
            animation: spin 2.5s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: auto;
        }

        .logo-container {
            background: #fff;
            padding: 10px 0;
            height: 50px;
        }

        .logo-container img {
            height: 40px;
            float: left;
        }

        header {
            background: #333;
            color: #fff;
            padding: 20px 0;
        }

        header h1 {
            float: left;
            margin: 0;
        }

        nav {
            float: right;
        }

        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        nav ul li {
            display: inline;
            margin-left: 20px;
        }

        nav ul li a {
            color: #fff;
            text-decoration: none;
            font-weight: bold;
        }

        .hero {
            position: relative;
            height: 500px;
            overflow: hidden;
            color: #fff;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .carousel {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
        }

        .carousel img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            animation: slide 15s infinite;
            opacity: 0;
        }

        .carousel img:nth-child(1) {
            animation-delay: 0s;
            opacity: 1;
        }

        .carousel img:nth-child(2) {
            animation-delay: 5s;
        }

        .carousel img:nth-child(3) {
            animation-delay: 10s;
        }

        @keyframes slide {
            0% { opacity: 0; }
            20% { opacity: 1; }
            33.33% { opacity: 1; }
            53.33% { opacity: 0; }
            100% { opacity: 0; }
        }
        .search-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .search-form {
            position: relative;
            z-index: 1;
        }

        .search-form input[type="text"] {
            padding: 10px;
            width: 300px;
            border: none;
            border-radius: 5px;
        }

        .search-form button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background: #ff5e3a;
            color: #fff;
            font-size: 1em;
            cursor: pointer;
        }

        .listings {
            padding: 50px 0;
            overflow-x: auto;
            white-space: nowrap;
        }

        .listing-grid {
            display: flex;
            gap: 20px;
            flex-wrap: nowrap;
        }

        .listing-card {
            background: #fff;
            padding: 40px;
            border: 1px solid #ddd;
            border-radius: 10px;
            width: 300px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .listing-card img {
            width: 100%;
            height: auto;
            max-height: 200px;
            border-radius: 10px;
        }

        .listing-card h3 {
            margin: 20px 0 10px;
        }

        .listing-card p {
            margin: 10px 0;
        }

        .listing-card button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background: #ff5e3a;
            color: #fff;
            font-size: 1em;
            cursor: pointer;
        }

        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 20px 0;
        }

        @media (max-width: 768px) {
            .listing-card {
                width: calc(50% - 20px);
            }
        }

        @media (max-width: 480px) {
            .listing-card {
                width: 100%;
            }

            nav ul li {
                display: block;
                text-align: center;
                margin: 10px 0;
            }

            header h1, nav {
                float: none;
                text-align: center;
            }

            .login-container {
                text-align: center;
                margin-top: 20px;
            }

            .login-container button {
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background: #ff5e3a;
                color: #fff;
                font-size: 1em;
                cursor: pointer;
            }

            .login-container a {
                display: block;
                margin-top: 10px;
                text-decoration: none;
                color: #fff;
                background: #333;
                padding: 10px 20px;
                border-radius: 5px;
            }

            .login-container a:hover {
                background: #555;
            }
        }
    </style>
</head>
<body>
<div id="preloader">
    <div class="preloader-content">
        <div class="preloader-image"></div>
        <div class="circle circle1"></div>
        <div class="circle circle2"></div>
        <div class="circle circle3"></div>
        <div class="circle circle4"></div>
    </div>
</div>

<div class="logo-container">
    <div class="container">
        <img src="logo1.jpg" alt="Logo">
    </div>
</div>
<header>
    <div class="container">
        <h1>Hostel & PG Tracker</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Search</a></li>
                <li><a href="contact.php">Contact</a></li>
            </ul>
        </nav>
    </div>
</header>
<h1>Welcome <?php echo $name; ?>!!</h1>
<section class="hero">
    <div class="carousel">
        <img src="ho2.jpg" alt="Hostel Image 2">
        <img src="ho1.jpg" alt="Hostel Image 3">
        <img src="ho4.jpg" alt="Hostel Image 4">
    </div>
    </section>
<br>
<footer>
    <div class="container">
        <p>&copy; 2024 Hostel & PG Tracker. All rights reserved.</p>
    </div>
</footer>

<script>
    // JavaScript to hide the preloader once the page is fully loaded with a minimum display time
    window.addEventListener('load', function() {
        const preloader = document.getElementById('preloader');
        const minTime = 3000; // Minimum display time in milliseconds (3 seconds)
        const loadTime = new Date().getTime() - performance.timing.navigationStart;

        if (loadTime < minTime) {
            setTimeout(() => {
                preloader.style.opacity = '0';
                preloader.style.visibility = 'hidden';
            }, minTime - loadTime);
        } else {
            preloader.style.opacity = '0';
            preloader.style.visibility = 'hidden';
        }
    });
</script>

</body>
</html>
