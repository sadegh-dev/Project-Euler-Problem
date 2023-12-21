package main

import "fmt"

func main() {

	fibo := []int{1, 2}
	index := 1
	new := 0
	total := 2

	for true {
		new = fibo[index] + fibo[index-1]

		if new > 10 {
			break
		} else {
			fibo = append(fibo, new)
			index += 1

			if new%2 == 0 {
				total += new
			}
		}
	}
	fmt.Println(fibo)
	fmt.Println(total)
}
