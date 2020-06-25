<?php

$code=$_POST["command"];
$exploded=explode("{",$code); 

$name=$exploded[0];
$name=str_replace("kubitsa:","",$name);
$name=trim($name);

$command=$exploded[1];
$command=str_replace("}","",$command);
$command=trim($command);

$filename = "saved/".$name.".bnx";

if (file_exists($filename)){
    unlink($filename);
}

file_put_contents($filename, ""); 
file_put_contents($filename, $command);

?>