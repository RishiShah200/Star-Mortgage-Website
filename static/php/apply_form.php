<?php

ini_set('SMTP', "smtp.gmail.com");
ini_set('smtp_port', "25");
ini_set('username',"hahsihsri@gmail.com");
ini_set('password','ihsri_hahs25');
ini_set('sendmail_from', "hahsihsri@gmail.com");

$errors = '';

$myemail = 'rishishah200@gmail.com';//<—–Put Your email address here. 


// if(empty($_POST['name']) ||empty($_POST['email']) || empty($_POST['message']) || empty($_POST['interest']) || empty($_POST['outreach'])){
//     $errors .= "\n All fields are required";
// }

$name = $_POST['name'];

$email_address = $_POST['email'];

$message = $_POST['message'];

$interest = $_POST['interest'];

$outreach = $_POST['outreach'];

// if (!preg_match("/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/i", $email_address)){
//     $errors .= "\n Error: Invalid email address";
// }

// if(empty($errors)){

    $to = $myemail;

    $email_subject = "Contact form submission: $name";

    $email_body = "You have received a new message. ".

    " Here are the details:\n Name: $name \n ".

    "Email: $email_address\n Message \n $message";

    $headers = "From: $myemail\n";

    $headers .= "Reply-To: $email_address";

    mail($to,$email_subject,$email_body,$headers);

    //redirect to the ‘thank you’ page

    header('Location: home.html');

// }
