<?php
// Database connection
$conn = new mysqli('localhost', 'root', '', 'admin_panel');

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve form data
$name = $_POST['name'];
$email = $_POST['email'];
$mobile = $_POST['mobile'];
$session_dates = implode(',', $_POST['session_dates']); // Convert array to comma-separated string
$address = $_POST['address'];
$event_type = $_POST['event_type'];
$package = $_POST['package'];

// Calculate payment amount based on package
$amount = 0;
switch ($package) {
    case 'Silver':
        $amount = 17500;
        break;
    case 'Golden':
        $amount = 40000;
        break;
    case 'Platinum':
        $amount = 72000;
        break;
   
}

// Insert data into the database
$sql = "INSERT INTO bookings (name, email, mobile, session_dates, address, event_type, package, amount)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

$stmt = $conn->prepare($sql);
$stmt->bind_param("sssssssi", $name, $email, $mobile, $session_dates, $address, $event_type, $package, $amount);

if ($stmt->execute()) {
    $booking_id = $stmt->insert_id;
} else {
    echo "Error: " . $stmt->error;
    $conn->close();
    exit();
}

// Close the database connection
$stmt->close();
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking Summary</title>
    <link rel="stylesheet" href="sty.css">
    <style>
        /* Center the main content */
        .bill-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: rgba(255, 255, 255, 0.2); 
            text-align: center;
        }

        /* Summary Container */
        .summary-container {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }

        /* Heading Styles */
        .summary-container h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }

        .summary-container h2 {
            font-size: 20px;
            margin-top: 20px;
            margin-bottom: 20px;
            color: #201E43;
        }

        /* Paragraph Styles */
        .summary-container p {
            margin-bottom: 10px;
            font-size: 16px;
        }

        /* Payment Form Styles */
        .summary-container form {
            margin-top: 20px;
        }

        .summary-container form input[type="radio"] {
            margin: 0 10px;
            cursor: pointer;
        }

        /* Button Styles */
        .summary-container form .btn {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #201E43;
            color: #fff;
            border: none;
            border-radius: 4px;
            text-decoration: none;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .summary-container form .btn:hover {
            background-color: #45a049;
        }

        /* Responsive Styles */
        @media (max-width: 768px) {
            .summary-container {
                width: 90%;
                padding: 15px;
            }

            .summary-container p {
                font-size: 14px;
            }

            .summary-container form .btn {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="bill-container">
        <div class="summary-container">
            <h1>Booking Summary</h1>
            <p><strong>Name:</strong> <?php echo htmlspecialchars($name); ?></p>
            <p><strong>Email:</strong> <?php echo htmlspecialchars($email); ?></p>
            <p><strong>Mobile:</strong> <?php echo htmlspecialchars($mobile); ?></p>
            <p><strong>Session Date:</strong> <?php echo htmlspecialchars($session_dates); ?></p>
            <p><strong>Address:</strong> <?php echo htmlspecialchars($address); ?></p>
            <p><strong>Event Type:</strong> <?php echo htmlspecialchars($event_type); ?></p>
            <p><strong>Package:</strong> <?php echo htmlspecialchars($package); ?></p>
            <p><strong>Amount:</strong> ₹<?php echo number_format($amount); ?></p>

            <form action="payment.php" method="POST">
                <input type="hidden" name="booking_id" value="<?php echo htmlspecialchars($booking_id); ?>">
                <input type="hidden" name="amount" value="<?php echo htmlspecialchars($amount); ?>">

                <button type="submit" class="btn">Proceed to Payment</button>
            </form>
        </div>
    </div>
</body>
</html>
