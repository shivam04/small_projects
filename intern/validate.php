<?php
function validate_email($email){
	if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  		$emailErr = "Invalid email format"; 
	}
	return $emailErr;
}

function validate_mobile($mobile){
	if(preg_match('/^\d{10}$/',$mobile)) // phone number is valid
    {
      $mobile = '0' . $mobile;

      // your other code here
    }
    else // phone number is not valid
    {
      return 'Phone number invalid !';
    }
}
?>