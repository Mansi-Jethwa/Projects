<?php
// Check if the payment form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve payment data
    $payment_method = htmlspecialchars($_POST['payment_method']);
    $total_price = htmlspecialchars($_POST['total_price']);

    // HTML header and styling
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Payment Confirmation</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #00072d;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                padding: 20px;
                max-width: 600px;
                width: 100%;
                text-align: center;
            }
            h1 {
                color: #00072d;
                margin-bottom: 20px;
            }
            p {
                color: #333;
                font-size: 18px;
                margin-bottom: 20px;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                color: #fff;
                background-color: #00072d;
                border: none;
                border-radius: 4px;
                text-decoration: none;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .btn:hover {
                background-color: #051650;
            }
        </style>
    </head>
    <body>
        <div class="container">';

    // Payment processing and confirmation message
    if ($payment_method == "Credit Card") {
        $card_name = htmlspecialchars($_POST['card_name']);
        $card_number = htmlspecialchars($_POST['card_number']);
        $exp_date = htmlspecialchars($_POST['exp_date']);
        $cvv = htmlspecialchars($_POST['cvv']);

        // Process the credit card payment here
        // ...

        echo '<h1>Credit Card Payment Successful</h1>';
        echo '<p>Thank you for your payment of ₹' . $total_price . '. Your transaction has been completed successfully.</p>';
    } elseif ($payment_method == "Net Banking") {
        $bank_name = htmlspecialchars($_POST['bank_name']);

        // Process the net banking payment here
        // ...

        echo '<h1>Net Banking Payment Successful</h1>';
        echo '<p>Thank you for your payment of ₹' . $total_price . ' with ' . $bank_name . '. Your transaction has been completed successfully.</p>';
    } else {
        echo '<h1>Invalid Payment Method</h1>';
        echo '<p>It seems there was an issue with the payment method selected. Please try again.</p>';
    }

    // Close HTML structure
    echo '<a href="index.php" class="btn">Return to Home</a>
        </div>
    </body>
    </html>';
}
?>
