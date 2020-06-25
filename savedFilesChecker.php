<?php

if ($handle = opendir('saved')) {

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {
	    $entry = str_replace(".bnx", "", $entry);
            echo "$entry\n";
        }
    }

    closedir($handle);
}

?>