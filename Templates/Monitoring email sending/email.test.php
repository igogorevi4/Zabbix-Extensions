<?php

require 'PHPMailer/PHPMailerAutoload.php';
$mail = new PHPMailer;
$mail->isSMTP();
$mail->setFrom('from@example.com', 'Test Subject');
$mail->addAddress('to@example.com', 'recieverName');
// Replace smtp_username with your Amazon SES SMTP user name.
$mail->Username = "YOURSESUSER";
$mail->Password = "YOURSESPASSWORD";
$mail->SMTPSecure = "ssl";
$mail->Port = 465;
$mail->From = "from@example.com";
$mail->FromName = "TestEmail";
// If you're using Amazon SES in a region other than US West (Oregon),
// replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
// endpoint in the appropriate region.
//$mail->Host = "email-smtp.eu-west-1.amazonaws.com";
$mail->Host = "email-smtp.eu-west-1.amazonaws.com";
$mail->Subject = 'Amazon SES test (SMTP interface accessed using PHP)';
$mail->Body = 'Sending... OK';
$mail->SMTPAuth = true;
$mail->SMTPSecure = 'ssl';
$mail->Port = 465;
$mail->SMTPDebug = 4;
// Tells PHPMailer to send HTML-formatted email
$mail->isHTML(true);
// The alternative email body; this is only displayed when a recipient
// opens the email in a non-HTML email client. The \r\n represents a
// line break.
$mail->AltBody = "Email Test\r\nThis email was sent through the
    Amazon SES SMTP interface using the PHPMailer class.";

if(!$mail->send()) {
    echo "Email not sent. " , $mail->ErrorInfo , PHP_EOL;
} else {
    echo "Email sent!" , PHP_EOL;
}
?>