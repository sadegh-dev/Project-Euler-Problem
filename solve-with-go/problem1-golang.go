package problem1

// Project Euler >> Problem 1

// Title: Multiples of 3 and 5

/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/

// Reference: https://projecteuler.net/problem=1

import (
	"fmt"
)

var (
	sum int
)

func problem1() {
	for numerator := 1; numerator < 1000; numerator++ {
		if numerator%3 == 0 || numerator%5 == 0 {
			sum += numerator
			fmt.Printf("%v ", numerator)
		}
	}
	fmt.Printf("\n sum = %v \n", sum)
}
