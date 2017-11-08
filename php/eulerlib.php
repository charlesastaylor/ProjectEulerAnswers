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

/**
 * Return permutations of given array
 * 
 * TODO: Not finished, made for p024 but can finished to make general
 */
function permutations($range, $used=array()) {
    global $perms; // erugh hack
    if (count($range) == count($used)) {
        array_push($perms, $used);
    } else {
        foreach($range as $i) {
            if (in_array($i, $used)) continue;
            array_push($used, $i);
            permutations($range, $used);
            array_pop($used);
        }
    }
}