<?php

$code=$_POST["command"];
$name=str_replace("gusiba:","",$code);
$name=trim($name);
$filename = "saved/".$name.".bnx";

if (file_exists($filename)){
    unlink($filename);
}


?>