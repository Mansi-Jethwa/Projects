<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set content type to image/jpeg
header("Content-type: image/jpeg");

// Create a blank image with true color
$width = 600;
$height = 400;
$image = imagecreatetruecolor($width, $height);

// Define colors
$white = imagecolorallocate($image, 255, 255, 255);
$black = imagecolorallocate($image, 0, 0, 0);
$blue = imagecolorallocate($image, 0, 51, 102);

// Fill the background with white
imagefilledrectangle($image, 0, 0, $width, $height, $white);

// Define the path to the sans-serif font
$font_path = __DIR__ . '/arial.ttf'; // Adjust path if necessary

// Check if the font file exists
if (!file_exists($font_path)) {
    die('Font file not found');
}

// Font size and positioning
$font_size = 16;
$title_font_size = 24;

// Retrieve payment data from query parameters
$payment_method = isset($_GET['payment_method']) ? htmlspecialchars($_GET['payment_method']) : 'Unknown';
$total_price = isset($_GET['total_price']) ? htmlspecialchars($_GET['total_price']) : '0';
$details = isset($_GET['details']) ? htmlspecialchars($_GET['details']) : 'No details';

// Add title
imagettftext($image, $title_font_size, 0, 20, 50, $blue, $font_path, "Payment Receipt");

// Add bill summary
imagettftext($image, $font_size, 0, 20, 100, $black, $font_path, "Bill Summary:");
imagettftext($image, $font_size, 0, 20, 130, $black, $font_path, "Method: $payment_method");
imagettftext($image, $font_size, 0, 20, 160, $black, $font_path, "Amount: ₹$total_price");
imagettftext($image, $font_size, 0, 20, 190, $black, $font_path, "Details: $details");

// Add payment method and amount
imagettftext($image, $font_size, 0, 20, 240, $black, $font_path, "Payment Method: $payment_method");
imagettftext($image, $font_size, 0, 20, 270, $black, $font_path, "Total Amount: ₹$total_price");

// Add footer with styling
imagettftext($image, $font_size, 0, 20, 320, $black, $font_path, "Thank you for your payment!");

// Output the image
imagejpeg($image, null, 90); // 90 is the quality setting

// Free up memory
imagedestroy($image);
?>
