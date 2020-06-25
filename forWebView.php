<!DOCTYPE html>
<html>
<head>
	<title>Benax</title>
	<link rel="shortcut icon" href="images/favicon.png">
	<link rel="stylesheet" href="css/app.css">
  <meta name="viewport" content = "width=device-width, initial-scale=1.0">

</head>

<body>

	<div id="loadPic">
		<div id="loadPicHeader">Ifoto
			<div id="closeButton" style="float: right; position: relative; z-index: 11; cursor: pointer; " onClick="hideAllThis();" ><img src="images/close.png" width="20px"/>
			</div>
		</div>
		<span id="load_pic">Loading</span>

	</div>


	<div id="benax-terminal-run-button"></div>

	<form method="post" id="codes_form">
	<textarea id="benax-terminal-textarea" name="codes" autofocus></textarea>
	</form>
	


	<!-- Last codes displayed -->
	<div id="last_codes">></div>
	<!-- /Last codes displayed -->

	<script src="js/jquery-2.2.3.js"></script>
	<script src="js/sendCodes.js"></script>
</body>
</html>
