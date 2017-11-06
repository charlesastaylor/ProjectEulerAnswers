<?php

/**
 * Problem 21 - Amicable numbers
 * 
 * Pretty straight forward brute force approach
 */

include 'eulerlib.php';

function d($n) {
    $divs = divisors($n);
    sort($divs);
    array_pop($divs);
    return array_sum($divs);
}

$amicable = array();

foreach(range(1,9999) as $a) {
    $b = d($a);
    if (d($b) == $a and $a != $b) {
        array_push($amicable, $a);
    }
}

echo array_sum($amicable);

