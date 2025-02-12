<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment</title>
    
    <style>
        /* General Styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    color: #333;
}

/* Payment Container */
.payment-container {
    width: 40%;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Heading Styles */
.payment-container h1 {
    text-align: center;
    color: #ff758c;
    margin-bottom: 20px;
}

/* Form Group */
.form-group {
    margin-bottom: 20px;
}

/* Label Styles */
.form-group label {
    display: block;
    margin-bottom: 5px;
    font-size:1rem;
    font-weight: bold;
    color: #555;
}

/* Radio Button Styles */
.radio-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.radio-group input[type="radio"] {
    margin-right: 0; /* Remove space between radio button and label */
    margin-left: 0; /* Add space between radio button and label */
}

.radio-group label {
    margin-left: 5px; /* Space between radio button and label */
}

/* Input and Select Styles */
.form-group input[type="text"],
.form-group input[type="month"],
.form-group input[type="radio"] {
    width: calc(100% - 22px); /* Adjust width for padding and border */
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
}

/* Radio Button Styles */
.form-group input[type="radio"] {
    width: auto;
    margin-right: 5px;
}

/* Button Styles */
.payment-container .btn {
    display: inline-block;
    width: 100%;
    padding: 10px 20px;
    color: #fff;
    background-color: #ff758c;
    border: none;
    border-radius: 4px;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.payment-container .btn:hover {
    background-color: #e84a65;
}

/* Responsive Styles */
@media (max-width: 768px) {
    .payment-container {
        width: 90%;
    }
    
    .form-group input[type="text"],
    .form-group input[type="month"] {
        width: calc(100% - 20px); /* Adjust width for padding and border */
    }

    .payment-container .btn {
        font-size: 14px;
        padding: 8px 16px;
    }
}


    </style>
</head>
<body>

<div class="payment-container">
    <h1>Payment Details</h1>
    <form action="payment_process.php" method="POST">
        
        <div class="form-group">
            <label>Select Payment Method:</label>
            <div class="radio-group">
                <input type="radio" id="creditCard" name="paymentMethod" value="Credit Card" required>
                <label for="creditCard">Credit Card</label>
                <input type="radio" id="debitCard" name="paymentMethod" value="Debit Card">
                <label for="debitCard">Debit Card</label>
            </div>
        </div>

        <div class="form-group">
            <label for="cardNumber">Card Number:</label>
            <input type="text" id="cardNumber" name="cardNumber" maxlength="16" oninput="this.value = this.value.replace(/\D/g, '');" required>
        </div>

        <div class="form-group">
            <label for="cardExpiry">Expiry Date:</label>
            <input type="month" id="cardExpiry" name="cardExpiry" required>
        </div>

        <div class="form-group">
            <label for="cardCVC">CVC:</label>
            <input type="text" id="cardCVC" name="cardCVC" maxlength="3" required oninput="this.value = this.value.replace(/[^0-9]/g, '');">
        </div>

        <div class="form-group">
            <label for="amount">Payment Amount:</label>
            <input type="text" id="amount" name="amount" readonly value="<?php echo $_POST['amount']; ?>">
        </div>

        <button type="submit" class="btn">Pay Now</button>
    </form>
</div>

</body>
</html>
