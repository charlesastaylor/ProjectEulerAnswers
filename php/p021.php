<?php

/**
 * Problem 21 - Amicable numbers
 * 
 * Pretty straight forward brute force approach
 */

function divisors($n) {
    $divs = array();
    if ($n == 0) return $divs;
    foreach (range(1, (int)sqrt($n)) as $x) {
        if ($n % $x === 0) {
            array_push($divs, $x);
            if ($n / $x !== $x) {
                array_push($divs, ($n / $x));
            }
        }
    }
    return $divs;
}

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

