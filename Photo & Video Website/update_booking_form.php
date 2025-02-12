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

// Get the booking ID from the query string
$booking_id = $_GET['id'] ?? '';

if ($booking_id) {
    // Fetch the booking details
    $sql = "SELECT * FROM bookings WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $booking_id);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $booking = $result->fetch_assoc();
    } else {
        echo "No booking found.";
        exit;
    }
} else {
    echo "Invalid booking ID.";
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Booking</title>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 90%;
            max-width: 800px;
            margin: 30px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        label {
            font-weight: bold;
            color: #555;
        }

        input, textarea {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            width: 100%;
            box-sizing: border-box;
        }

        textarea {
            resize: vertical;
            height: 100px;
        }

        button.btn {
            padding: 10px 15px;
            font-size: 16px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
            width: 100%;
            box-sizing: border-box;
        }

        button.btn:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }

        .btn-container {
            text-align: center;
            margin-top: 20px;
        }

        .btn-container a {
            display: inline-block;
            padding: 10px 15px;
            font-size: 16px;
            color: #007bff;
            text-decoration: none;
            border: 1px solid #007bff;
            border-radius: 4px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .btn-container a:hover {
            background-color: #007bff;
            color: #fff;
        }
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
</head>
<body>
    <div class="container">
        <h1>Update Booking</h1>
        <form action="process_update.php" method="POST">
            <input type="hidden" name="id" value="<?php echo htmlspecialchars($booking['id']); ?>">
            
            <label for="name">Username:</label>
            <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($booking['name']); ?>" required readonly>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($booking['email']); ?>" required>
            
            <label for="mobile">Mobile:</label>
            <input type="text" id="mobile" name="mobile" value="<?php echo htmlspecialchars($booking['mobile']); ?>" required>
            
            <!-- Session Dates -->
            <label for="session_dates">Session Dates:</label>
            <input type="text" id="session_dates" name="session_dates" value="<?php echo htmlspecialchars($booking['session_dates']); ?>" required>
            
            <label for="address">Address:</label>
            <textarea id="address" name="address" required><?php echo htmlspecialchars($booking['address']); ?></textarea>
            
            <label for="event_type">Event Type:</label>
            <input type="text" id="event_type" name="event_type" value="<?php echo htmlspecialchars($booking['event_type']); ?>" required>
            
            <label for="package">Package:</label>
            <input type="text" id="package" name="package" value="<?php echo htmlspecialchars($booking['package']); ?>" required>
            
            <label for="amount">Amount:</label>
            <input type="number" id="amount" name="amount" step="0.01" value="<?php echo htmlspecialchars($booking['amount']); ?>" required>
            
            <button type="submit" class="btn">Update Booking</button>
        </form>
        <div class="btn-container">
            <a href="booking_history.php" class="btn">Back to Booking History</a>
        </div>
    </div>

    <!-- Include jQuery and Datepicker -->
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

    <script>
        // Enable multiple date selection
        $(function() {
            $("#session_dates").datepicker({
                dateFormat: 'yy-mm-dd',
                numberOfMonths: 2,
                onSelect: function(dateText, inst) {
                    var dates = $("#session_dates").val();
                    if (dates !== '') {
                        dates += ',' + dateText;
                    } else {
                        dates = dateText;
                    }
                    $("#session_dates").val(dates);
                },
                beforeShowDay: function(date) {
                    var selectedDates = $("#session_dates").val().split(',');
                    var currentDate = $.datepicker.formatDate('yy-mm-dd', date);
                    return [selectedDates.indexOf(currentDate) == -1];
                }
            });
        });
    </script>
</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
