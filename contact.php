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
    background-image: url('back1.jpg'); /* Replace 'background-image.jpg' with the path to your image */
    background-size: cover;
    background-position: center;
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
        }

        .carousel img:nth-child(2) {
            animation-delay: 5s;
        }

        .carousel img:nth-child(3) {
            animation-delay: 10s;
        }

        .carousel img:nth-child(4) {
            animation-delay: 15s;
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
            padding: 20px;
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

        .form-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 50px auto;
        }

        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input[type="text"],
        .form-group input[type="email"],
        .form-group input[type="tel"],
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }

        .form-group input[type="submit"] {
            background-color: #ff5e3a;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            width: 100%;
        }

        .form-group input[type="submit"]:hover {
            background-color: #e04a26;
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

            .form-container {
                width: 90%;
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
                    <li><a href="index.php">Home</a></li>
                    <li><a href="#">Search</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="form-container">
        <h2>Contact Form</h2>
        <form action="#" method="post">
            <div class="form-group">
                <label for="name">Your Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="city">City:</label>
                <input type="text" id="city" name="city" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required>
                <small>Format: 123-456-7890</small>
            </div>
            <div class="form-group">
                <label for="message">Your Message/Query:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <div class="form-group">
                <input type="submit" value="Submit">
            </div>
        </form>
    </div>

    <footer>
        <div class="container">
            <p>&copy; 2024 Hostel & PG Tracker. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
