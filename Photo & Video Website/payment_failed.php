<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Failed</title>
    <link rel="stylesheet" href="style.css">
    <style>
        /* General reset */
body, h1, p {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    line-height: 1.6;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    overflow: hidden;
}

.payment-container {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 100%;
    max-width: 400px;
}

.payment-container h1 {
    margin-bottom: 20px;
    font-size: 24px;
    color: #4CAF50; /* Green color for success */
}

.payment-container p {
    margin-bottom: 10px;
    font-size: 16px;
}

.payment-container .btn {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 4px;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.payment-container .btn:hover {
    background-color: #45a049;
}

.payment-container .btn-secondary {
    background-color: #f44336; /* Red color for failure */
}

.payment-container .btn-secondary:hover {
    background-color: #e53935;
}

/* Input fields for payment form */
.payment-form input[type="text"], 
.payment-form input[type="number"], 
.payment-form input[type="email"], 
.payment-form input[type="date"], 
.payment-form input[type="time"], 
.payment-form input[type="password"], 
.payment-form select {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

.payment-form label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.payment-form .form-group {
    margin-bottom: 15px;
}

.payment-form .error {
    color: red;
    font-size: 12px;
    display: none;
}

.payment-container .form-group {
    text-align: left;
}

.payment-container .form-group .error {
    margin-top: 5px;
}

.payment-container h1.error-title {
    color: #f44336; /* Red color for error messages */
}

    </style>
</head>
<body>

<div class="payment-container">
    <h1>Payment Failed</h1>
    <p>Unfortunately, your payment could not be processed. Please try again.</p>
    <a href="payment.php" class="btn">Try Again</a>
</div>

</body>
</html>
