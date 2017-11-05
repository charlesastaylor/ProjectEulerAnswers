<?php

/**
 * Problem 20 - Factorial digit sum
 * 
 * Lul php can only store 32bit ints. Gonna do this one in python rather than
 * have to deal with keeping track of big ints manually.
 */

 function factorial($n) {
     if ($n === 1) {
         return 1;
     } else {
         return $n * factorial($n - 1);
     }
}

echo factorial(100);