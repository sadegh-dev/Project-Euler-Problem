package main

import "fmt"

func main() {

	fibo := []int{1, 2}
	index := 1
	new := 0
	total := 0

	for true {
		new = fibo[index] + fibo[index-1]

		if new > 1000 {
			break
		} else {
			fibo = append(fibo, new)
			index += 1
		}
	}
	fmt.Println(fibo)
	fmt.Println(total)
}
