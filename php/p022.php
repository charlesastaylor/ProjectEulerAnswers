<?php

/**
 * Problem 22 - Names scores
 */

$file = fopen("p022_names.txt", "r");
$names_string = fgets($file);
$names_array = explode(",", $names_string);
sort($names_array) or die("sort failed");
$total = 0;
foreach($names_array as $key => $name) {
    $value = 0;
    echo $key . " " . $name . " ";
    foreach(str_split($name) as $char) {
        $value += ord($char) - 96;
        echo $char . " " . $value . " | ";
    }
    $total += $value * ($key + 1);
    // echo $total;
}
echo $total;