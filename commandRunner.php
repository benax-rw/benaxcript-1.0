<?php
file_put_contents('executor.py', ""); 
$header = "import functions as y\nfrom functions import *\ninit()\n\n";
file_put_contents('executor.py', $header);

$code=$_POST["command"];
$explosion0 = explode(":",$code);
$called_name=trim($explosion0[1]); //something like function_name(t=2)

if(strpos($command,'burundu:') !== false){
	$explosion1 = explode("(",$called_name);
	$function_name = $explosion1[0]; //something like function_name
	$argument = $explosion1[1]; //something like t=2)
	$argument = str_replace(')', '',$argument); //something like t=2

	$explosion2 = explode("=",$argument);
	$param = $explosion2[0]; //something like t
	$arg = $explosion2[1];  //something like 2
	file_put_contents('executor.py', $param."=".$arg."\n", FILE_APPEND);

	$saved_name = $function_name."(".$param.")";
	$filename = "saved/".$saved_name.".bnx";
}
else{
$filename = "saved/".$called_name.".bnx";		
}
$command = file_get_contents($filename);
include "interpret.php";

?>
