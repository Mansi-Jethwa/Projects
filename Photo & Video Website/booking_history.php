<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header('Location: login.php');
    exit;
}

// Database connection details
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "admin_panel";

// Create a new connection to the MySQL server
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the logged-in user's name from the session
$user_name = $_SESSION['username'];

// Fetch the booking history for the logged-in user
$sql = "SELECT id, name, email, mobile, session_dates, address, event_type, amount, cancellation_status, notification FROM bookings WHERE name = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $user_name);
$stmt->execute();
$result = $stmt->get_result();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking History</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px;
        }
        h1 {
            color: #333;
            margin-bottom: 30px;
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
        }
        .card-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
        .card {
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 30%;
            max-width: 900px;
            transition: box-shadow 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
        }
        .card-content {
            font-size: 0.95em;
            color: #555;
            margin-bottom: 20px;
        }
        .card-content label {
            font-weight: 600;
            color: #333;
            margin-right: 10px;
        }
        .actions {
            display: flex;
            gap: 10px;
            justify-content: center;
        }
        .actions form {
            margin: 0;
        }
        button.btn {
            padding: 12px 25px;
            font-size: 0.9em;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button.btn:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        footer {
            background-color: #333;
            color: #fff;
            padding: 20px 0;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
            box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
        }
        .message {
            text-align: center;
            margin-bottom: 20px;
            font-size: 1.1em;
            color: #28a745;
        }
        .error-message {
            color: #dc3545;
        }
        .back-button {
            display: inline-block;
            padding: 12px 25px;
            margin-top: 30px;
            font-size: 0.9em;
            color: #fff;
            background-color: #6c757d;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .back-button:hover {
            background-color: #5a6268;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Your Booking History</h1>
        <?php if (isset($_GET['status']) && $_GET['status'] === 'requested'): ?>
            <div class="message">Cancellation request has been sent to the admin.</div>
        <?php endif; ?>
        <div class="card-container">
            <?php while ($row = $result->fetch_assoc()): ?>
                <div class="card">
                    <div class="card-content">
                        <!-- Display notification if there is one -->
                        <?php if (!empty($row['notification'])): ?>
                            <p class="message"><?php echo htmlspecialchars($row['notification']); ?></p>
                        <?php endif; ?>
                        <p><label>Name:</label><?php echo htmlspecialchars($row['name']); ?></p>
                        <p><label>Email:</label><?php echo htmlspecialchars($row['email']); ?></p>
                        <p><label>Mobile:</label><?php echo htmlspecialchars($row['mobile']); ?></p>
                        
                        <!-- Display multiple session dates -->
<p><label>Session Dates:</label> 
<?php
$session_dates = explode(',', $row['session_dates']);
foreach ($session_dates as $date) {
    echo htmlspecialchars($date) . "<br>";
}
?>
</p>

                        

                        <p><label>Address:</label><?php echo htmlspecialchars($row['address']); ?></p>
                        <p><label>Event Type:</label><?php echo htmlspecialchars($row['event_type']); ?></p>
                        
                        <p><label>Amount:</label>$<?php echo htmlspecialchars(number_format($row['amount'], 2)); ?></p>
                        <p><label>Cancellation Status:</label><?php echo htmlspecialchars($row['cancellation_status']); ?></p>
                        
                        <!-- Display message based on cancellation status -->
                        <?php if ($row['cancellation_status'] === 'Approved'): ?>
                            <p class="message">Your payment will be refunded within 24 hours.</p>
                        <?php elseif ($row['cancellation_status'] === 'Rejected'): ?>
                            <p class="error-message">Your cancellation request was rejected. If you still want to cancel the order, you will only receive a 50% refund.</p>
                            <form action="request_cancel_booking.php" method="POST">
                                <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                                <button type="submit" class="btn">Cancel Order</button>
                            </form>
                        <?php endif; ?>
                    </div>
                    <div class="actions">
                        <?php if ($row['cancellation_status'] === 'Pending'): ?>
                            <p>Cancellation Requested</p>
                        <?php elseif ($row['cancellation_status'] !== 'Approved' && $row['cancellation_status'] !== 'Rejected'): ?>
                            <form action="update_booking_form.php" method="GET">
                                <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                                <button type="submit" class="btn">Update</button>
                            </form>
                            <form action="request_cancel_booking.php" method="POST">
                                <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                                <button type="submit" class="btn">Request Cancel</button>
                            </form>
                        <?php endif; ?>
                    </div>
                </div>
            <?php endwhile; ?>
        </div>
        <div class="message">
            <a href="index.php" class="back-button">Back to Home</a>
        </div>
    </div>
</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
