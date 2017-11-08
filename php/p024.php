<?php

/**
 * Problem 24- Lexicographic Permutation
 * 
 * Pretty awful hacky solution but gives answer.
 */

function permhack($range, $used=array()) {
    global $count;
    if (count($range) == count($used)) {
        if(++$count == 1000000) { // millionth
            foreach($used as $i) {
                echo $i;
            }
            die("");
        }
    } else {
        foreach($range as $i) {
            if (in_array($i, $used)) continue;
            array_push($used, $i);
            permhack($range, $used);
            array_pop($used);
        }
    }
}

$count = 0;
permhack(range(0,9));
