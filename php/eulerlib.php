<?php

/**
 * Common functions for project euler problems
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