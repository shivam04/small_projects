<?php
	require 'validate.php';
	if(isset($_POST['name'])&&isset($_POST['zip'])&&isset($_POST['city'])&&isset($_POST['state'])&&
		isset($_POST['email'])&&isset($_POST['address'])&&isset($_POST['mobile']))	{
		$name = $_POST['name'];
		$zip = $_POST['zip'];
		$city = $_POST['city'];
		$state = $_POST['state'];
		$email = $_POST['email'];
		$address = $_POST['address'];
		$mobile= $_POST['mobile'];
		$e =  $state=="Select State";
		if(empty($name)){
			$name_error = "Name Required";
		}if(empty($zip)){
			$zip_error = "Zip Code Required";
		}if(empty($city)){
			$city_error = "City Required";
		}if(empty($state)||$e==1){
			$state_error = "State Required";
		}if(empty($email)){
			$email_error = "Email Required";
		}if(empty($address)){
			$address_error = "Address Required";
		}if(empty($mobile)){
			$mobile_error = "Mobile Number Required";
		}
		if(empty($name_error)&&empty($zip_error)&&empty($city_error)&&empty($state_error)&&
			empty($email_error)&&empty($address_error)&&empty($mobile_error)){
			$email_error = validate_email($email);
			$mobile_error = validate_mobile($mobile);
			if(empty($email_error)&&empty($mobile_error)){
					header("Location:done.php");
			}
			
		}
	}
?>
<!-- DOCTYPE HTML -->
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="bootstrap-theme.css">
		<link rel="stylesheet" type="text/css" href="bootstrap-theme.min.css">
		<link rel="stylesheet" type="text/css" href="bootstrap.css">
		<link rel="stylesheet" type="text/css" href="bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="form.css">
		<title> Billing Details </title>
	</head>
	<body>
		<div class="container">
			<form action='' method='post' role="form" class="form-horizontal">
				<h2> Billing Detail </h2>
				<div class='form-group'>
					<label class="col-sm-3 control-label">Name:* </label>
					<div class="col-sm-9">
						<input class="form-control" type="text" name="name">
						<?php if(!empty($name_error)) echo '<h6 class="alert alert-danger">'.$name_error.'</h6>'; ?>
					</div>
				</div>	
				<div class='form-group'>
					<label class="col-sm-3 control-label" for="name"  >Zip Code:* </label>
					<div class="col-sm-9">
						<input class="form-control" type="text" name="zip">
						<?php if(!empty($zip_error)) echo '<h6 class="alert alert-danger">'.$zip_error.'</h6>'; ?>
					</div>

				</div>
				<div class='form-group'>
					<label class="col-sm-3 control-label">City:* </label>

					<div class="col-sm-9">
						<input class="form-control" type="text" name="city">
						<?php if(!empty($city_error)) echo '<h6 class="alert alert-danger">'.$city_error.'</h6>'; ?>
					</div>
				</div>
				<div class='form-group'>
					<label class="col-sm-3 control-label">State:* </label>
					<div class="col-sm-9">
						<select name="state" class="form-control">
							<option>Select State</option>
							<option>Andhra Pradesh</option>
							<option>Arunachal Pradesh</option>
							<option>Himachal Pradesh</option>
							<option>Madhya Pradesh</option>
							<option>Uttar Pradesh</option>
						</select>
						<?php if(!empty($state_error)) echo '<h6 class="alert alert-danger">'.$state_error.'</h6>'; ?>
					</div>
				</div>
				<div class='form-group'>
					<label class="col-sm-3 control-label">Address:* </label>
					<div class="col-sm-9">
						<input class="form-control" type="text" name="address">
						<?php if(!empty($address_error)) echo '<h6 class="alert alert-danger">'.$address_error.'</h6>'; ?>
					</div>
				</div>
				<div class='form-group'>
					<label class="col-sm-3 control-label">Email:* </label>
					<div class="col-sm-9">
						<input class="form-control" type="text" name="email">
						<?php if(!empty($email_error)) echo '<h6 class="alert alert-danger">'.$email_error.'</h6>'; ?>
					</div>
				</div>
				<div class='form-group'>
					<label class="col-sm-3 control-label">Mobile:* </label>
					<div class="col-sm-9">
						<input class="form-control" type="text" name="mobile">
					<?php if(!empty($mobile_error)) echo '<h6 class="alert alert-danger">'.$mobile_error.'</h6>'; ?>
					</div>
				</div>
				<div class="form-group">
	        		<div class="col-sm-9 col-sm-offset-3">
						<input class="btn btn-primary btn-block" type="submit" value="Submit">
					</div>
				</div>
			</form>
		</div>
	
	</body>
</html>