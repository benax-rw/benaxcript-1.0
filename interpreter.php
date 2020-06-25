<?php

$command=$_POST["command"];
file_put_contents('executor.py', ""); 
$header = "import functions as y\nfrom functions import *\ninit()\n\n";
file_put_contents('executor.py', $header);
include "interpret.php";
?>
