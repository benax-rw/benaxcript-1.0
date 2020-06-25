<!DOCTYPE html>
<html>
<head>
	<title>Benax Terminal</title>
	<link rel="shortcut icon" href="images/favicon.png">
	<link rel="stylesheet" href="css/style.css">
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
	
	<div class="benax-terminal-top"><a href="/.">BenaXcript</a></div>
	<div spellcheck="false" class="benax-terminal-div">
	<div id="benax-terminal-run-button"></div>
	
	<form method="post" id="codes_form">
	<textarea id="benax-terminal-textarea" name="codes" autofocus></textarea>
	</form>
	
	<!-- Last codes displayed -->
	<div id="last_codes">>
	
	</div>
	<span style='float: right; font-size: 12px; '><a href='touch-stop-script.php'>Hagarika!</a></span>
	<!-- /Last codes displayed -->
	</div>
	
	<script src="js/jquery-2.2.3.js"></script>
	<script src="js/sendCodes.js"></script>
	<script type="application/javascript" src="https://api.ipify.org?format=jsonp&callback=getIP"></script>
</body>
</html>
