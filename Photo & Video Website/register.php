<?php
require 'config.php';

$error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = $_POST['password'];
    $confirmPassword = $_POST['confirm_password'];

    // Check if username is empty
    if (empty($username)) {
        $error = "Username is required";
    } elseif (strlen($username) < 4) {
        $error = "Username must be at least 4 characters long";
    }

    // Check if passwords match
    if (empty($password) || empty($confirmPassword)) {
        $error = "Password and Confirm Password fields are required";
    } elseif ($password !== $confirmPassword) {
        $error = "Passwords do not match";
    } elseif (strlen($password) < 4) {
        $error = "Password must be at least 4 digits long";
    }

    if (empty($error)) {
        // Check if username already exists
        $sql = "SELECT id FROM users WHERE username = ?";
        $stmt = $conn->prepare($sql);

        if ($stmt === false) {
            die('Prepare failed: ' . htmlspecialchars($conn->error));
        }

        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            $error = "Username already taken";
        } else {
            // Hash the password
            $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

            // Prepare SQL statement
            $sql = "INSERT INTO users (username, password) VALUES (?, ?)";
            $stmt = $conn->prepare($sql);

            if ($stmt === false) {
                die('Prepare failed: ' . htmlspecialchars($conn->error));
            }

            // Bind parameters
            $bind = $stmt->bind_param("ss", $username, $hashedPassword);

            if ($bind === false) {
                die('Bind failed: ' . htmlspecialchars($stmt->error));
            }

            // Execute the statement
            $exec = $stmt->execute();

            if ($exec) {
                header("Location: login.php");
                exit();
            } else {
                $error = "Error: " . htmlspecialchars($stmt->error);
            }

            // Close the statement
            $stmt->close();
        }
    }
}

// Close the connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="st.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
    $(document).ready(function() {
        // Clear error message when user types in the input field
        $("#username, #password, #confirm_password").on("input", function() {
            $(this).next(".error").text("");
        });

        $("#register-button").on("click", function(event) {
            var isValid = true;

            // Validate username
            var username = $("#username").val().trim();
            if (username === "") {
                $("#username").next(".error").text("Username is required");
                isValid = false;
            }

            // Validate password
            var password = $("#password").val();
            if (password === "") {
                $("#password").next(".error").text("Password is required");
                isValid = false;
            } else if (password.length < 4) {
                $("#password").next(".error").text("Password must be at least 4 digits long");
                isValid = false;
            }

            // Validate confirm password
            var confirmPassword = $("#confirm_password").val();
            if (confirmPassword === "") {
                $("#confirm_password").next(".error").text("Confirm Password is required");
                isValid = false;
            } else if (password !== confirmPassword) {
                $("#confirm_password").next(".error").text("Passwords do not match");
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault(); // Prevent form submission
            }
        });
    });
</script>

</head>
<body>
    <div class="container">
        <h2>Register</h2>
        <?php if ($error): ?>
            <p class="error"><?= $error ?></p>
        <?php endif; ?>
        <form id="register-form" action="register.php" method="post">
            <table>
                <tr>
                    <td><label for="username">Username:</label></td>
                    <td>
                        <input type="text" id="username" name="username" required>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password:</label></td>
                    <td>
                        <input type="password" id="password" name="password" required pattern="\d{4}" title="Please enter a 4-digit password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="confirm_password">Confirm Password:</label></td>
                    <td>
                        <input type="password" id="confirm_password" name="confirm_password" required pattern="\d{4}" title="Please enter a 4-digit password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td colspan="2"><button type="submit" id="register-button">Register</button></td>
                </tr>
            </table>
        </form>
        <a href="login.php">Login</a>
    </div>
</body>
</html>
