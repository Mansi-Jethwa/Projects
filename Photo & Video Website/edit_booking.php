<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header('Location: login.php');
    exit;
}

// Fetch booking details from session
if (!isset($_SESSION['booking'])) {
    echo "No booking details found.";
    exit;
}

$booking = $_SESSION['booking'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Booking</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <?php include 'header.php'; ?>
    </header>
    <main>
        <h1>Edit Booking</h1>
        <form action="update_booking_action.php" method="POST">
            <input type="hidden" name="booking_id" value="<?php echo htmlspecialchars($booking['booking_id']); ?>">
            <label>Name:</label>
            <input type="text" name="name" value="<?php echo htmlspecialchars($booking['name']); ?>" required>
            <label>Email:</label>
            <input type="email" name="email" value="<?php echo htmlspecialchars($booking['email']); ?>" required>
            <label>Mobile:</label>
            <input type="text" name="mobile" value="<?php echo htmlspecialchars($booking['mobile']); ?>" required>
            <label>Session Date:</label>
            <input type="date" name="session_date" value="<?php echo htmlspecialchars($booking['session_date']); ?>" required>
            <label>Session Time Start:</label>
            <input type="time" name="session_time_start" value="<?php echo htmlspecialchars($booking['session_time_start']); ?>" required>
            <label>Session Time End:</label>
            <input type="time" name="session_time_end" value="<?php echo htmlspecialchars($booking['session_time_end']); ?>" required>
            <label>Address:</label>
            <textarea name="address" required><?php echo htmlspecialchars($booking['address']); ?></textarea>
            <label>Event Type:</label>
            <input type="text" name="event_type" value="<?php echo htmlspecialchars($booking['event_type']); ?>" required>
            <label>Package:</label>
            <input type="text" name="package" value="<?php echo htmlspecialchars($booking['package']); ?>" required>
            <label>Amount:</label>
            <input type="number" name="amount" value="<?php echo htmlspecialchars($booking['amount']); ?>" step="0.01" required>
            <button type="submit" class="btn">Update Booking</button>
        </form>
    </main>
</body>
</html>
