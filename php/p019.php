<?php

/**
 * Problem 19 - Counting Sundays
 * 
 * I'm quite sure there is a nice method of solving this, probably using 
 * modular arithmetic. I'm going to brute force it instead.
 */
$daysInMonth = array(
    1 => 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
);

// Monday = 0, .. , Sunday = 6
define("SUNDAY", 6);
$dayOfWeek = 1;  // 1/1/1901 was a tuesday
$noSundays = 0;

foreach (range(1901, 2000) as $year) {
    // check for leap year
    if ($year % 4 === 0 and ($year % 100 !== 0 or $year % 400 === 0)) {
        $daysInMonth[2] = 29;
    } else {
        $daysInMonth[2] = 28;
    }
    
    foreach(range(1,12) as $month) {
        foreach(range(1,$daysInMonth[$month]) as $day) {
            if ($day === 1 and $dayOfWeek === SUNDAY) {
                ++$noSundays;
            }
            $dayOfWeek = ($dayOfWeek + 1) % 7;
        }
    }
}

echo $noSundays;
