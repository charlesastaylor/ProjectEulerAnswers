<?php

/**
 * Problem 23 - Non-abundant sums
 * 
 * Crude, slow bruteforce solve
 */

include 'eulerlib.php';

function isAbundant($n) {
    $sum = 0;
    foreach(divisors($n) as $i) {
        if ($i == $n) {
            continue; // only care about proper divisors
        }
        $sum += $i;
    }
    return $sum > $n;
}

// return array of abundant numbers <= n
function abundantNumbers($n) {
    $numbers = array();
    foreach(range(1,$n) as $i) {
        if (isAbundant($i)) {
            array_push($numbers, $i);
        }
    }
    return $numbers;
}

$abunNums = abundantNumbers(28123);
$cant = range(0,28128);

foreach($abunNums as $i) {
    foreach($abunNums as $j) {
        unset($cant[$i + $j]);
    }
}

echo array_sum($cant);
