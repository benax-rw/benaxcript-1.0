<?php

$code=$_POST["command"];
$name=str_replace("kubikuza:","",$code);
$name=trim($name);
$filename = "saved/".$name.".bnx";
echo file_get_contents($filename);

?>