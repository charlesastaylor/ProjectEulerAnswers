<?php

/**
 * Problem 22 - Names scores
 * 
 * Straight forward handling files, strings etc.
 */

$file = fopen("p022_names.txt", "r");
$names_string = fgets($file);
$names_array = explode(',', $names_string);
sort($names_array) or die("sort failed");
$total = 0;
foreach($names_array as $key => $name) {
    // first format the strings correctly
    $name = strtolower(trim($name, '"'));

    $value = 0;
    foreach(str_split($name) as $char) {
        $value += ord($char) - 96;
    }
    $total += $value * ($key + 1);
}
echo $total;