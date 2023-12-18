package problem2

func main() {

	fibo := []int{1, 2}
	index := 1
	new := 0

	for true {
		new = fibo[index] + fibo[index-1]

		if new > 100 {
			break
		} else {
			fibo = append(fibo, new)
		}
	}

}
